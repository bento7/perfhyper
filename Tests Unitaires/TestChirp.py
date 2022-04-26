import unittest
from Post_Traitements.Chirp import chirp
import numpy as np


class Testchirp(unittest.TestCase):

    def test_norm(self):
        chirp1 = chirp(15000e6, '../data/200Hz_10cm.txt', 3.296e-7)
        norm1, norm2 = chirp1.norm(0)
        self.assertEqual(np.max(norm1),1.)
        self.assertEqual(np.max(norm2),1.)
        sig1 = chirp1.Msent[0].reshape((-1,1))[:,0]/max(chirp1.Msent[0].reshape((-1,1))[:,0])
        self.assertTrue(np.allclose(sig1,norm1))

    def test_correlate(self):
        chirp1 = chirp(15000e6, '../data/200Hz_10cm.txt', 3.296e-7)
        selfcor, intercor = chirp1.correlate(0)
        Msent, Mrec = chirp1.norm(0)
        selfcor1 = np.correlate(Msent, Msent, 'full') * chirp1.T
        result = []
        for i in range(len(selfcor)):
            result.append(selfcor[i]==selfcor1[i])
        self.assertTrue(all(result))

    def test_CFAR(self):
        chirp1 = chirp(15000e6, '../data/200Hz_10cm.txt', 3.296e-7)
        signal0, signal1 = chirp1.correlate(0)
        nb_entrainement = 0.08 * len(signal0)
        nb_garde = nb_entrainement // 4
        taux_fa = 1e-5
        CFAR = chirp1.CFAR(signal1, nb_entrainement, nb_garde, taux_fa)
        self.assertEqual(CFAR[0],5116)

    def test_distance(self):
        chirp1 = chirp(15000e6, '../data/200Hz_10cm.txt', 3.296e-7)
        signal0, signal1 = chirp1.correlate(0)
        distance = chirp1.distance(signal0, signal1)
        self.assertEqual(distance,1.73)


if __name__ == '__main__':
    unittest.main()




