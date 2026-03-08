import pandas as pd
import numpy as np
from pathlib import Path
import json

# load series function
def load_series(path):
    # load 
    df = pd.read_csv(path)
    
    # validate columns
    required_columns = {"timestamp", "value"}
    missing_columns = required_columns - set(df.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns : {missing_columns}")

    # parse timestamp and value 
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df["value"] = pd.to_numeric(df["value"], errors="coerce")

    df = df.dropna(subset=["timestamp", "value"])

    # sort by timestamp
    df = df.sort_values(by='timestamp')

    df = df.drop_duplicates(subset=["timestamp"], keep="first")

    df = df.reset_index(drop=True)

    if df.empty:
        raise ValueError("Series is empty after cleaning")

    return df

def load_dataset(directory):
    root_dir = Path(directory)
    series_dict = {}

    for csv in root_dir.rglob("*.csv"):
        relative_path = csv.relative_to(root_dir).as_posix()
        series_dict[relative_path] = load_series(csv)

    return series_dict

def load_combined_windows(labels_path):
    labels_path = Path(labels_path)

    with open(labels_path, "r", encoding="utf-8") as f:
        windows = json.load(f)
    return windows

