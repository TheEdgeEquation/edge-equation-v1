from typing import Any, Dict, List
from .base_source import BaseSource


class NBASource(BaseSource):
    sport = "nba"

    def fetch(self) -> List[Dict[str, Any]]:
        from ingestion.sample_loader import load_sample_raw
        return load_sample_raw(self.sport)

    def metadata(self) -> Dict[str, Any]:
        return {
            "sport": self.sport,
            "provider": "SAMPLE_NBA_PROVIDER",
            "version": "v1",
        }
