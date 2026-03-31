import json
from pathlib import Path
import pandas as pd
from joblib import load

def run_inference(input_csv: str, model_dir: str) -> pd.DataFrame:
    model = load(Path(model_dir) / "model.joblib")

    with open(Path(model_dir) / "metadata.json", "r") as f:
        metadata = json.load(f)

    df = pd.read_csv(input_csv)
    X = df[metadata["columns"]].fillna(0.0)

    scores = model.decision_function(X)
    preds = model.predict(X)

    out = df.copy()
    out["anomaly_score"] = scores
    out["anomaly_flag"] = (preds == -1).astype(int)
    return out