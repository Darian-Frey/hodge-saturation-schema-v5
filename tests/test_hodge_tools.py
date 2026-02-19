import unittest
import numpy as np
from tools.ghost_cycle_tracker import NCTransferMap
from tools.nc_correspondence import NCCorrespondence
from tools.galois_action_sim import GaloisGroupSim
from tools.global_verifier import SnInvarianceVerifier

class TestHodgeTools(unittest.TestCase):

    def test_o_minimal_bound(self):
        tracker = NCTransferMap(variety_type="K3xK3")
        self.assertIsNotNone(tracker.simulate_lift(1.0, t_parameter=0.5))
        self.assertIsNone(tracker.simulate_lift(1.0, t_parameter=1e-500))

    def test_nc_correspondence_composition(self):
        corr = NCCorrespondence("S1", "S2")
        composition = corr.compose(NCCorrespondence("S2", "S3"))
        self.assertEqual(composition.source, "S1")
        self.assertEqual(composition.target, "S3")

    def test_galois_invariance(self):
        sim = GaloisGroupSim(rank=22)
        v_hodge = np.zeros(22)
        v_hodge[0] = 1.0 
        identity = np.eye(22)
        self.assertTrue(sim.is_invariant(v_hodge, identity))

    def test_sn_invariance_logic(self):
        """Verifies that symmetric tensors pass and asymmetric tensors fail."""
        n, dim = 2, 22
        verifier = SnInvarianceVerifier(n_points=n, dimension_per_factor=dim)
        
        # Case A: Invariant (v ⊗ v)
        v = np.zeros(dim)
        v[21] = 1.0
        v_tensor_v = np.outer(v, v).flatten()
        self.assertTrue(verifier.verify_bkb_compatibility(v_tensor_v))
        
        # Case B: Non-invariant (v ⊗ w)
        w = np.zeros(dim)
        w[0] = 1.0
        v_tensor_w = np.outer(v, w).flatten()
        self.assertFalse(verifier.verify_bkb_compatibility(v_tensor_w))

if __name__ == '__main__':
    unittest.main()
