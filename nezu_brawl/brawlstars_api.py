# nezu_brawl/brawlstars_api.py

import os
import requests
from dotenv import find_dotenv, load_dotenv
from typing import Dict, Any

from nezu_brawl.url import (
    get_brawler_info_url,
    get_brawler_rankings_url,
    get_brawlers_url,
    get_club_info_url,
    get_club_members_url,
    get_club_rankings_url,
    get_event_rotation_url,
    get_player_battlelog_url,
    get_player_info_url,
    get_player_rankings_url,
)


class BrawlStarsAPI:
    def __init__(
        self, player_tag: str, club_tag: str, country_code: str, brawler_id: str
    ) -> None:
        """
        Initialize the BrawlStarsAPI class with necessary parameters.

        :param player_tag: Player tag for Brawl Stars
        :param club_tag: Club tag for Brawl Stars
        :param country_code: Country code for rankings
        :param brawler_id: Brawler ID for detailed info
        """
        load_dotenv(find_dotenv())  # Load .env file
        self.api_key: str = os.getenv("API_KEY")  # Get API_KEY from .env
        self.player_tag: str = player_tag  # Player tag
        self.club_tag: str = club_tag  # Club tag
        self.country_code: str = country_code  # Country code
        self.brawler_id: str = brawler_id  # Brawler ID

    def _get_headers(self) -> Dict[str, str]:
        """Create headers for the API request."""
        return {"Authorization": f"Bearer {self.api_key}"}

    def _make_request(self, url: str) -> Dict[str, Any]:
        """Make a GET request to the given URL and handle errors."""
        try:
            response = requests.get(url, headers=self._get_headers())
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}  # Return error message as a dictionary

    def get_player_battlelog(self) -> Dict[str, Any]:
        """Get player battle log."""
        url = get_player_battlelog_url(self.player_tag)
        return self._make_request(url)

    def get_player_info(self) -> Dict[str, Any]:
        """Get player information."""
        url = get_player_info_url(self.player_tag)
        return self._make_request(url)

    def get_club_members(self) -> Dict[str, Any]:
        """Get club members."""
        url = get_club_members_url(self.club_tag)
        return self._make_request(url)

    def get_club_info(self) -> Dict[str, Any]:
        """Get club information."""
        url = get_club_info_url(self.club_tag)
        return self._make_request(url)

    def get_club_rankings(self) -> Dict[str, Any]:
        """Get club rankings."""
        url = get_club_rankings_url(self.country_code)
        return self._make_request(url)

    def get_brawler_rankings(self) -> Dict[str, Any]:
        """Get brawler rankings."""
        url = get_brawler_rankings_url(self.country_code, self.brawler_id)
        return self._make_request(url)

    def get_player_rankings(self) -> Dict[str, Any]:
        """Get player rankings."""
        url = get_player_rankings_url(self.country_code)
        return self._make_request(url)

    def get_brawlers(self) -> Dict[str, Any]:
        """Get list of available brawlers."""
        url = get_brawlers_url()
        return self._make_request(url)

    def get_brawler_info(self) -> Dict[str, Any]:
        """Get information about a specific brawler."""
        url = get_brawler_info_url(self.brawler_id)
        return self._make_request(url)

    def get_event_rotation(self) -> Dict[str, Any]:
        """Get event rotation."""
        url = get_event_rotation_url()
        return self._make_request(url)
