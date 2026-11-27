import pandas as pd
from pathlib import Path


DATA_PATH = Path(__file__).resolve().parent.parent / "human_activity_recognition.csv"
META_COLS = ["subject_id", "activity_id", "activity", "dataset_split"]

def load_data(path = DATA_PATH) :
    "load the data set"
    return pd.read_csv(path)


def split_data(df):
    "split data into train , test data"
    train = df[df["dataset_split"] == "train"]
    test = df[df["dataset_split"] == "test"]

    X_train = train.drop(columns = META_COLS)
    y_train = train['activity']
    groups_train = train["subject_id"]

    X_test = test.drop(columns=META_COLS)
    y_test = test["activity"]

    return X_train, y_train, groups_train, X_test, y_test

def check_data(df) :
    "quality checks for the data"
    print("Shape:", df.shape)
    print("Duplicate rows:", df.duplicated().sum())
    print("Missing values:", df.isnull().sum().sum())
    



if __name__ == "__main__":
    df = load_data()
    check_data(df)
    X_train, y_train, groups_train, X_test, y_test = split_data(df)
    print("Train:", X_train.shape, "Test:", X_test.shape)
    
    train_ids = set(groups_train)
    test_ids = set(df.loc[X_test.index, "subject_id"])
    print("Volunteers:", len(train_ids), "train,", len(test_ids), "test")
    print("Overlap:", train_ids & test_ids)