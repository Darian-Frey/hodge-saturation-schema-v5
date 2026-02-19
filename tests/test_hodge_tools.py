import unittest
import numpy as np
from tools.ghost_cycle_tracker import NCTransferMap
from tools.nc_correspondence import NCCorrespondence
from tools.galois_action_sim import GaloisGroupSim

class TestHodgeTools(unittest.TestCase):

    def test_o_minimal_bound(self):
        tracker = NCTransferMap(variety_type="K3xK3")
        # Test a valid lift (low complexity)
        self.assertIsNotNone(tracker.simulate_lift(1.0, t_parameter=0.5))
        # Test an invalid lift (boundary case/high complexity)
        # In our script, complexity = |ln(t)|. 
        # t=1e-500 would exceed the 1000 bound.
        self.assertIsNone(tracker.simulate_lift(1.0, t_parameter=1e-500))

    def test_nc_correspondence_composition(self):
        corr = NCCorrespondence("S1", "S2")
        composition = corr.compose(NCCorrespondence("S2", "S3"))
        self.assertEqual(composition.source, "S1")
        self.assertEqual(composition.target, "S3")

    def test_galois_invariance(self):
        sim = GaloisGroupSim(rank=22)
        v_hodge = np.zeros(22)
        v_hodge[0] = 1.0 # Standard algebraic class (e.g., hyperplane section)
        identity = np.eye(22)
        self.assertTrue(sim.is_invariant(v_hodge, identity))

if __name__ == '__main__':
    unittest.main()
