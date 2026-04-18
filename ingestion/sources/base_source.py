from abc import ABC, abstractmethod
from typing import Any, Dict, List


class BaseSource(ABC):
    sport: str

    @abstractmethod
    def fetch(self) -> List[Dict[str, Any]]:
        """Fetch raw records from upstream source."""
        raise NotImplementedError

    @abstractmethod
    def metadata(self) -> Dict[str, Any]:
        """Return source metadata (provider, sport, version, etc.)."""
        raise NotImplementedError
