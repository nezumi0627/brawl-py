# main.py
# sample\test.py
import os

import requests
from dotenv import find_dotenv, load_dotenv

from nezu_brawl.url import get_player_info_url

# Load .env file
load_dotenv(find_dotenv())

# API key and tags
API_KEY = os.getenv("API_KEY")  # Get API_KEY from .env
PLAYER_TAG = "%23PQ0J8VJUY"  # Player tag with %23


def get_brawl_info(player_tag):
    """Get player information from the API."""
    try:
        # Create headers for the API request
        headers = {"Authorization": f"Bearer {API_KEY}"}

        # Get player information
        player_info_url = get_player_info_url(player_tag)
        player_info_response = requests.get(player_info_url, headers=headers)
        player_info_response.raise_for_status()

        # Get the JSON response
        player_info = player_info_response.json()
        print(player_info)

        # Print player information in a formatted way
        print(f"\{player_info['name']}({player_info['tag']})")
        print(f"総トロフィー: {player_info['trophies']}")
        print(f"最高トロフィー: {player_info['highestTrophies']}")
        print(f"expLevel: {player_info['expLevel']}")
        print(f"expPoints: {player_info['expPoints']}")
        print(f"3v3勝利数: {player_info['3vs3Victories']}")
        print(f"solo勝利数: {player_info['soloVictories']}")
        print(f"duo勝利数: {player_info['duoVictories']}")
        print("\nclub情報:")
        print(f"{player_info['club']['name']}({player_info['club']['tag']})")

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    get_brawl_info(PLAYER_TAG)


if __name__ == "__main__":
    main()
