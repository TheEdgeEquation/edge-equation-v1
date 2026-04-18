import json
from pathlib import Path
from typing import Any, Dict, List

from ingestion.config import DATA_RAW_DIR


def load_sample_raw(sport: str) -> List[Dict[str, Any]]:
    """Load sample raw data for a given sport."""
    file_path = DATA_RAW_DIR / f"{sport}.json"

    if not file_path.exists():
        return []

    with open(file_path, "r") as f:
        return json.load(f)
