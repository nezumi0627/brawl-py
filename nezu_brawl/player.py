# nezu_brawl/player.py

from typing import Any, Dict

from nezu_brawl.url import (
    get_player_battlelog_url,
    get_player_info_url,
    get_player_rankings_url,
)

from .api_base import BrawlStarsAPIBase


class PlayerAPI(BrawlStarsAPIBase):
    def __init__(self, player_tag: str) -> None:
        """Initialize the PlayerAPI class with player tag."""
        super().__init__()  # Initialize the base class
        self.player_tag: str = player_tag  # Player tag

    def get_battlelog(self) -> Dict[str, Any]:
        """Get player battle log."""
        url = get_player_battlelog_url(self.player_tag)
        return self._make_request(url)

    def get_info(self) -> Dict[str, Any]:
        """Get player information."""
        url = get_player_info_url(self.player_tag)
        return self._make_request(url)

    def get_rankings(self, country_code: str) -> Dict[str, Any]:
        """Get player rankings."""
        url = get_player_rankings_url(country_code)
        return self._make_request(url)
