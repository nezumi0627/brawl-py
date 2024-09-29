# nezu_brawl/club.py

from typing import Any, Dict

from nezu_brawl.url import (
    get_club_info_url,
    get_club_members_url,
    get_club_rankings_url,
)

from .api_base import BrawlStarsAPIBase


class ClubAPI(BrawlStarsAPIBase):
    def __init__(self, club_tag: str) -> None:
        """Initialize the ClubAPI class with club tag."""
        super().__init__()  # Initialize the base class
        self.club_tag: str = club_tag  # Club tag

    def get_info(self) -> Dict[str, Any]:
        """Get club information."""
        url = get_club_info_url(self.club_tag)
        return self._make_request(url)

    def get_members(self) -> Dict[str, Any]:
        """Get club members."""
        url = get_club_members_url(self.club_tag)
        return self._make_request(url)

    def get_rankings(self, country_code: str) -> Dict[str, Any]:
        """Get club rankings."""
        url = get_club_rankings_url(country_code)
        return self._make_request(url)
