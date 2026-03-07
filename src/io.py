import pandas as pd

def load_series(path):

    df = pd.read_csv(path)

    required_columns = {"timestamp", "value"}
    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        raise ValueError(f"Missing required columns : {missing_columns}")

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    if not df["timestamp"].is_monotonic_increasing:
        df.sort_values(by='timestamp', inplace=True)

    df = df.drop_duplicates(subset=["timestamp"], keep="first")

    df["value"] = pd.to_numeric(df["value"], errors="coerce")

    df.reset_index(drop=True, inplace=True)

    return df
