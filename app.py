from fastapi import FastAPI
import pandas as pd
import json
from pathlib import Path

app = FastAPI()

DATASET_PATH = Path("/mnt/data")

@app.get("/read-csv")
def read_csv(filename: str):
    file_path = DATASET_PATH / filename
    df = pd.read_csv(file_path)
    return {
        "filename": filename,
        "columns": df.columns.tolist(),
        "rows": df.to_dict(orient="records")
    }

@app.get("/read-json")
def read_json(filename: str):
    file_path = DATASET_PATH / filename
    with open(file_path, "r") as f:
        data = json.load(f)
    return {
        "filename": filename,
        "content": data
    }
