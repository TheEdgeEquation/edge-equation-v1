from typing import Any, Dict, List


def normalize_records(records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Normalize raw records into a consistent schema."""
    normalized = []

    for r in records:
        normalized.append(
            {
                "game_id": r.get("game_id"),
                "home_team": r.get("home_team"),
                "away_team": r.get("away_team"),
                "home_score": r.get("home_score"),
                "away_score": r.get("away_score"),
            }
        )

    return normalized
