import unittest
from Post_Traitements.Chirp import chirp
import numpy as np


class Testchirp(unittest.TestCase):
    chirp1 = chirp(15000e6, '../data/essai_reflecteur_1.txt', 3.296e-7)

    def test_norm(self):
        norm1, norm2 = chirp1.norm(0)
        self.assertEqual(np.max(norm1),1.)
        self.assertEqual(np.max(norm2),1.)
        sig1 = chirp1.Msent[0].reshape((-1,1))[:,0]/max(chirp1.Msent[0].reshape((-1,1))[:,0])
        self.assertTrue(np.allclose(sig1,norm1))

    def test_correlate(self):
        selfcor, intercor = chirp1.correlate(0)
        
        pass

    def test_CFAR(self):
        pass

    def test_distance(self):
        pass


if __name__ == '__main__':
    unittest.main()




