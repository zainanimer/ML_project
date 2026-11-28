import time
from pathlib import Path
import joblib
import pandas as pd

from prepration import load_data

STREAM_PATH = Path(__file__).resolve().parent / "live_streamed.csv"
MODEL_PATH = Path(__file__).resolve().parent / "ridge_model.pkl"
META_COLS = ["subject_id", "activity_id", "activity", "dataset_split"]
POLL_INTERVAL = 0.5


def run_live_predictions(
    stream_path: Path = STREAM_PATH,
    model_path: Path = MODEL_PATH,
    poll_interval: float = POLL_INTERVAL,
) -> None:
    model = joblib.load(model_path)
    df_all = load_data()
    expected_total = len(df_all[df_all["dataset_split"] == "test"])

    seen_rows = 0
    correct_count = 0

    print("Waiting for live_streamed.csv updates...")

    while True:
        if stream_path.exists() and stream_path.stat().st_size > 0:
            live_df = pd.read_csv(stream_path)
            current_rows = len(live_df)

            if current_rows > seen_rows:
                new_rows = live_df.iloc[seen_rows:current_rows]
                X_new = new_rows.drop(columns=META_COLS, errors="ignore")
                preds = model.predict(X_new)

                has_actual = "activity" in new_rows.columns
                actuals = new_rows["activity"].tolist() if has_actual else [None] * len(preds)

                for idx, (pred, actual) in enumerate(zip(preds, actuals), start=seen_rows + 1):
                    if actual is not None:
                        is_match = pred == actual
                        if is_match:
                            correct_count += 1
                        acc_so_far = (correct_count / idx) * 100
                        status = "OK" if is_match else "MISS"
                        print(
                            f"[{idx}/{expected_total}] Pred: {pred} | Actual: {actual} "
                            f"({status}) | Running Acc: {acc_so_far:.2f}%"
                        )
                    else:
                        print(f"[{idx}/{expected_total}] Pred: {pred}")

                seen_rows = current_rows

            if seen_rows >= expected_total and expected_total > 0:
                print("Finished processing all streamed rows.")
                break

        time.sleep(poll_interval)


if __name__ == "__main__":
    try:
        run_live_predictions()
    except KeyboardInterrupt:
        print("Live prediction stopped.")