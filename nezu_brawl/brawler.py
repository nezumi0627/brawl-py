# nezu_brawl/brawler.py

from typing import Any, Dict

from nezu_brawl.url import (
    get_brawler_info_url,
    get_brawler_rankings_url,
    get_brawlers_url,
)

from .api_base import BrawlStarsAPIBase


class BrawlerAPI(BrawlStarsAPIBase):
    def __init__(self, brawler_id: str) -> None:
        """Initialize the BrawlerAPI class with brawler ID."""
        super().__init__()  # Initialize the base class
        self.brawler_id: str = brawler_id  # Brawler ID

    def get_info(self) -> Dict[str, Any]:
        """Get information about a specific brawler."""
        url = get_brawler_info_url(self.brawler_id)
        return self._make_request(url)

    def get_rankings(self, country_code: str) -> Dict[str, Any]:
        """Get brawler rankings."""
        url = get_brawler_rankings_url(country_code, self.brawler_id)
        return self._make_request(url)

    def get_all(self) -> Dict[str, Any]:
        """Get list of available brawlers."""
        url = get_brawlers_url()
        return self._make_request(url)
