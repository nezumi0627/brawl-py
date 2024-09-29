# sample\test.py
# main.py
# sample\test.py
import os

import requests
from dotenv import find_dotenv, load_dotenv

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

# Load .env file
load_dotenv(find_dotenv())

# API key and tags
API_KEY = os.getenv("API_KEY")  # Get API_KEY from .env
PLAYER_TAG = "%23PQ0J8VJUY"  # Player tag with %23
CLUB_TAG = "%232V08RLQJ0"  # Club tag with %23
COUNTRY_CODE = "ja"  # Example country code
BRAWLER_ID = "16000000"  # Replace with an actual brawler ID


def get_headers():
    """Create headers for the API request."""
    return {"Authorization": f"Bearer {API_KEY}"}


def main():
    try:
        # Get player battle log
        battlelog_url = get_player_battlelog_url(PLAYER_TAG)
        battlelog_response = requests.get(battlelog_url, headers=get_headers())
        battlelog_response.raise_for_status()
        print("Player Battle Log:", battlelog_response.json())

        # Get player information
        player_info_url = get_player_info_url(PLAYER_TAG)
        player_info_response = requests.get(player_info_url, headers=get_headers())
        player_info_response.raise_for_status()
        print("\nPlayer Information:", player_info_response.json())

        # Get club members
        club_members_url = get_club_members_url(CLUB_TAG)
        club_members_response = requests.get(club_members_url, headers=get_headers())
        club_members_response.raise_for_status()
        print("\nClub Members:", club_members_response.json())

        # Get club information
        club_info_url = get_club_info_url(CLUB_TAG)
        club_info_response = requests.get(club_info_url, headers=get_headers())
        club_info_response.raise_for_status()
        print("\nClub Information:", club_info_response.json())

        # Get club rankings
        club_rankings_url = get_club_rankings_url(COUNTRY_CODE)
        club_rankings_response = requests.get(club_rankings_url, headers=get_headers())
        club_rankings_response.raise_for_status()
        print("\nClub Rankings:", club_rankings_response.json())

        # Get brawler rankings
        brawler_rankings_url = get_brawler_rankings_url(COUNTRY_CODE, BRAWLER_ID)
        brawler_rankings_response = requests.get(
            brawler_rankings_url, headers=get_headers()
        )
        brawler_rankings_response.raise_for_status()
        print("\nBrawler Rankings:", brawler_rankings_response.json())

        # Get player rankings
        player_rankings_url = get_player_rankings_url(COUNTRY_CODE)
        player_rankings_response = requests.get(
            player_rankings_url, headers=get_headers()
        )
        player_rankings_response.raise_for_status()
        print("\nPlayer Rankings:", player_rankings_response.json())

        # Get list of available brawlers
        brawlers_url = get_brawlers_url()
        brawlers_response = requests.get(brawlers_url, headers=get_headers())
        brawlers_response.raise_for_status()
        print("\nAvailable Brawlers:", brawlers_response.json())

        # Get information about a specific brawler
        brawler_info_url = get_brawler_info_url(BRAWLER_ID)
        brawler_info_response = requests.get(brawler_info_url, headers=get_headers())
        brawler_info_response.raise_for_status()
        print("\nBrawler Information:", brawler_info_response.json())

        # Get event rotation
        event_rotation_url = get_event_rotation_url()
        event_rotation_response = requests.get(
            event_rotation_url, headers=get_headers()
        )
        event_rotation_response.raise_for_status()
        print("\nEvent Rotation:", event_rotation_response.json())

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
