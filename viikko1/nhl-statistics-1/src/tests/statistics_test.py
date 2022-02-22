import unittest
from statistics import Statistics
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

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_finds_player(self):
        player = self.statistics.search("Semenko")

        self.assertAlmostEqual(player.name, "Semenko")
        self.assertAlmostEqual(player.assists, 12)

    def test_search_returns_none_when_no_player(self):
        player = self.statistics.search("null")

        self.assertAlmostEqual(player, None)

    def test_team_can_be_found(self):
        team = self.statistics.team("EDM")

        self.assertAlmostEqual(team[1].name, "Kurri")
        self.assertAlmostEqual(team[2].team, "EDM")

    def test_top_scorers_works(self):
        top = self.statistics.top_scorers(2)

        self.assertAlmostEqual(top[0].name, "Gretzky")
        self.assertAlmostEqual(top[1].name, "Lemieux")
