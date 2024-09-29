"""
nezu_brawl - A Python library for accessing the Brawl Stars official API.

Author: nezumi0627
Version: 1.0.0
"""

from .api_base import BrawlStarsAPIBase
from .brawler import BrawlerAPI
from .club import ClubAPI
from .event import EventAPI
from .player import PlayerAPI

__author__ = "nezumi0627"
__version__ = "1.0.0"

__all__ = [
    "BrawlStarsAPIBase",
    "BrawlerAPI",
    "ClubAPI",
    "EventAPI",
    "PlayerAPI",
]
