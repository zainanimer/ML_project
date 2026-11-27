import time 
from pathlib import Path

from prepration import load_data

STREAM_PATH = Path(__file__).resolve().parent /"live_streamed.csv"
DELAY = 1.28

def stream_data(df , path = STREAM_PATH , delay = DELAY) : 
    test = df[df['dataset_split'] == "test"]
    test.head(0).to_csv(path , index = False)

    for i in range(len(test)) : 
        row = test.iloc[[i]]
        row.to_csv(path , mode = "a" , header = False , index = False)
        print(f"sent row {i +1} /{len(test)}")
        time.sleep(delay)

if __name__ == "__main__":
    df = load_data()
    try:
        stream_data(df)
    except KeyboardInterrupt:
        print("Stream stopped.")