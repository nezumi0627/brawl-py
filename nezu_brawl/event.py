# nezu_brawl/event.py

from typing import Any, Dict

from nezu_brawl.url import get_event_rotation_url

from .api_base import BrawlStarsAPIBase


class EventAPI(BrawlStarsAPIBase):
    def get_rotation(self) -> Dict[str, Any]:
        """Get event rotation."""
        url = get_event_rotation_url()
        return self._make_request(url)
