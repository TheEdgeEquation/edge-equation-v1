from pathlib import Path

# Base data directory (relative to repo root)
REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = REPO_ROOT / "data"
DATA_RAW_DIR = DATA_DIR / "raw"
DATA_NORMALIZED_DIR = DATA_DIR / "normalized"

# Default sports
SPORTS = ["mlb", "nba", "nhl"]
