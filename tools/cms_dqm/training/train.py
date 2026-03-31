import json
from pathlib import Path
from sklearn.ensemble import IsolationForest
from joblib import dump

from tools.cms_dqm.data.loaders import load_tabular_dqm_data

def train_baseline_model(input_csv: str, output_dir: str) -> None:
    df = load_tabular_dqm_data(input_csv)
    X = df.select_dtypes(include=["number"]).fillna(0.0)

    model = IsolationForest(random_state=42)
    model.fit(X)

    outdir = Path(output_dir)
    outdir.mkdir(parents=True, exist_ok=True)

    dump(model, outdir / "model.joblib")
    with open(outdir / "metadata.json", "w") as f:
        json.dump(
            {
                "model_type": "IsolationForest",
                "n_features": X.shape[1],
                "columns": list(X.columns),
            },
            f,
            indent=2,
        )