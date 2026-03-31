from pathlib import Path
import pandas as pd

def load_tabular_dqm_data(path: str) -> pd.DataFrame:
    """
    Load tabular CMS DQM-style data.
    Placeholder loader for prototype workflows.
    """
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    if file_path.suffix == ".csv":
        return pd.read_csv(file_path)

    raise ValueError(f"Unsupported file type: {file_path.suffix}")