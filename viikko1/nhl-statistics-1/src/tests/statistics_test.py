import unittest
from statistics import Statistics
from player import Player
from enum import Enum

class PlayerReaderStub:

    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class SortByStub(Enum):
    POINT = 1
    GOALS = 2
    ASSISTS = 3
    OTHER = 4


class TestStatistics(unittest.TestCase):

    def setUp(self):
        self.stats = Statistics(PlayerReaderStub())

    def test_search_returns_player(self):
        player = self.stats.search("Semenko")

        self.assertEqual(player.name, "Semenko")

    def test_search_nonexistent_player_returns_none(self):
        player = self.stats.search("Selanne")

        self.assertIsNone(player)

    def test_team_returns_correct_amount_of_players(self):
        team = self.stats.team("EDM")

        self.assertEqual(len(team), 3)

    def test_top_players_ordered_by_points(self):
        top_players = self.stats.top(2, SortByStub.POINT)

        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Lemieux")

    def test_top_players_ordered_by_goals(self):
        top_players = self.stats.top(2, SortByStub.GOALS)

        self.assertEqual(top_players[0].name, "Lemieux")
        self.assertEqual(top_players[1].name, "Yzerman")

    def test_top_players_ordered_by_assists(self):
        top_players = self.stats.top(2, SortByStub.ASSISTS)

        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Yzerman")

    def test_incorrect_ordering_criteria_raises_exception(self):
        with self.assertRaises(Exception):
            self.stats.top(2, SortByStub.OTHER)