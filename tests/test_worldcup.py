# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
import unittest
from WorldCup import GROUPS, simulate

class WorldCupTests(unittest.TestCase):
    def test_roster(self):
        self.assertEqual(len(GROUPS), 8)
        self.assertEqual(len({team for teams in GROUPS.values() for team in teams}), 32)
    def test_deterministic(self):
        self.assertEqual(simulate(42), simulate(42))
    def test_winner_is_valid(self):
        winner, lines = simulate(123)
        self.assertIn(winner, {team for teams in GROUPS.values() for team in teams})
        self.assertTrue(any("Final" == line for line in lines))
    def test_rounds(self):
        _, lines = simulate(42)
        self.assertEqual(sum(" vs " in line for line in lines), 15)

if __name__ == "__main__":
    unittest.main()
