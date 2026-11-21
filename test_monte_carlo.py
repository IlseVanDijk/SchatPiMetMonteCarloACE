"""De voorbeeldtest uit de opdracht."""

import unittest

from monte_carlo import estimate_pi


class TestMonteCarlo(unittest.TestCase):
    def test_voorbeeld_met_vaste_seed(self):
        self.assertEqual(estimate_pi(4, 42), 3.0)
