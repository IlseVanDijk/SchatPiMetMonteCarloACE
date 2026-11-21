"""De voorbeeldtest uit de opdracht."""

import unittest

from monte_carlo import estimate_pi
from monte_carlo import is_in_unit_circle


class TestMonteCarlo(unittest.TestCase):
    def test_voorbeeld_met_vaste_seed(self):
        self.assertEqual(estimate_pi(4, 42), 3.0, "Code is fout")
    def test_op_rand(self):
        self.assertEqual(is_in_unit_circle(0,1), True, "Op de rand worden punten niet geteld")
    def test_negatief_op_rand(self):
        self.assertEqual(is_in_unit_circle(-1,0), True, "Negatief op de rand wordt niet geteld")
    def test_negatief_buiten_cirkel(self):
        self.assertEqual(is_in_unit_circle(-1,-1), False, "Negatieve punten buiten de cirkel worden als erin geteld")

#Hieronder worden de tests uitgevoerd
if __name__ == '__main__':
    unittest.main()