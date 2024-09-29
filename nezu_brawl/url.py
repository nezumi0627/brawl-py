# nezu_brawl/url.py

BASE_URL = "https://api.brawlstars.com/v1"


def get_player_battlelog_url(player_tag: str) -> str:
    """Get the URL for player battle log."""
    return f"{BASE_URL}/players/{player_tag}/battlelog"


def get_player_info_url(player_tag: str) -> str:
    """Get the URL for player information."""
    return f"{BASE_URL}/players/{player_tag}"


def get_club_members_url(club_tag: str) -> str:
    """Get the URL for club members."""
    return f"{BASE_URL}/clubs/{club_tag}/members"


def get_club_info_url(club_tag: str) -> str:
    """Get the URL for club information."""
    return f"{BASE_URL}/clubs/{club_tag}"


def get_club_rankings_url(country_code: str) -> str:
    """Get the URL for club rankings."""
    return f"{BASE_URL}/rankings/{country_code}/clubs"


def get_brawler_rankings_url(country_code: str, brawler_id: str) -> str:
    """Get the URL for brawler rankings."""
    return f"{BASE_URL}/rankings/{country_code}/brawlers/{brawler_id}"


def get_player_rankings_url(country_code: str) -> str:
    """Get the URL for player rankings."""
    return f"{BASE_URL}/rankings/{country_code}/players"


def get_brawlers_url() -> str:
    """Get the URL for available brawlers."""
    return f"{BASE_URL}/brawlers"


def get_brawler_info_url(brawler_id: str) -> str:
    """Get the URL for specific brawler information."""
    return f"{BASE_URL}/brawlers/{brawler_id}"


def get_event_rotation_url() -> str:
    """Get the URL for event rotation."""
    return f"{BASE_URL}/events/rotation"
