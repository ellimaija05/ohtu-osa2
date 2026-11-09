import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_existing_player(self):
        player = self.stats.search("Kurri")
        self.assertEqual(player.name, "Kurri")

    def test_search_non_existing_player(self):
        player = self.stats.search("Selänne")
        self.assertIsNone(player)

    def test_team_players(self):
        edm_players = self.stats.team("EDM")
        self.assertEqual(len(edm_players), 3)

    def test_top_scorers(self):
        top = self.stats.top(1)
        self.assertEqual(top[0].name, "Gretzky")
