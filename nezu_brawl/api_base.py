# nezu_brawl/api_base.py

import os
from typing import Any, Dict

import requests
from dotenv import find_dotenv, load_dotenv


class BrawlStarsAPIBase:
    def __init__(self) -> None:
        """Initialize the base class and load the API key."""
        load_dotenv(find_dotenv())  # Load .env file
        self.api_key: str = os.getenv("API_KEY")  # Get API_KEY from .env

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
