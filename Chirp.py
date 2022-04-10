import numpy as np
import scipy
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt
from scipy import signal
import util as u
import position as pos

class chirp():

    def __init__(self, fsamp, path, T_chirp):
        self.fsamp = fsamp
        self.path = path
        self.T_chirp = T_chirp
        self.T = 1/self.fsamp
        """Extraction of the data"""
        self.sent, self.rec = u.load(path)
        """Matrix format"""
        self.Msent = u.SignalToMatrix(self.sent, self.fsamp, self.T_chirp)
        self.Mrec = u.SignalToMatrix(self.rec, self.fsamp, self.T_chirp)


    def norm(self,num):
        print(np.max(chirp500.Msent))
        print(np.max(chirp500.Mrec))

        """
        fonction servant à normaliser les amplitudes du signal émis et reçu pour pouvoir
        les comparer correctement. Leurs amplitudes diffèrent grandement initialement.
        :para num: Numéro du chirp envoyé dans la salve
        """
        Msent_norm = self.Msent[num].reshape((-1, 1))[:, 0] / max(self.Msent[num].reshape((-1, 1))[:, 0])
        Mrec_norm = self.Mrec[num].reshape((-1, 1))[:, 0] / max(self.Mrec[num].reshape((-1, 1))[:, 0])
        return Msent_norm, Mrec_norm


    def correlate(self,num):
        Msent, Mrec = self.norm(num)
        selfcor = np.correlate(Msent,Msent,'full')*self.T
        intercor = np.correlate(Mrec,Msent,'full')*self.T
        return selfcor, intercor

    def CFAR(self, signal, nb_entrainement, nb_garde, taux_fa):
        """
        :param signal: Données à traiter
        :param nb_entrainement: Nombre de cellules d'entraînement
        :param nb_garde: Nombre de cellule de garde
        :param taux_fa: Taux de fausse alarme
        :return: liste des pics détéctés
        """

        # Nombre total de cellules
        nb_cellules = signal.size
        # Taille de la zone de gardes à l'avant et à l'arrière de la cellule testée
        nb_garde_demi = round(nb_garde / 2)
        # Taille de zone d'entraînement à l'avant et à l'arrière de la cellule testée
        nb_entrainement_demi = round(nb_entrainement / 2)
        # Taille de la zone de travail à l'avant et à l'arrière de la cellule testée
        nb_cote = nb_garde_demi + nb_entrainement_demi

        # Facteur de seuil
        alpha = nb_entrainement * (taux_fa ** (-1 / nb_entrainement) - 1)

        idx_pics = []
        for i in range(nb_cote, nb_cellules - nb_cote):
            # Vérifie que la cellule considérée n'est pas un extremum local

            if i != i - nb_cote + np.argmax(signal[i - nb_cote:i + nb_cote + 1]):
                continue

            # Somme des valeurs de toutes les cellules entrant de le calcul courant
            somme1 = np.sum(signal[i - nb_cote:i + nb_cote + 1])
            # Somme des valeurs comprises dans la zone de garde
            somme2 = np.sum(signal[i - nb_garde_demi:i + nb_garde_demi + 1])
            # Calcul du bruit en foction des valeurs présentent dans les cellules d'entrainement uniquement
            p_bruit = (somme1 - somme2) / nb_entrainement
            # Calcul de la valeur de seuil
            seuil = alpha * p_bruit

            if (signal[i] > seuil):
                idx_pics.append(i)  # Stockage des indices des pics

        idx_pics = np.array(idx_pics, dtype=int)
        return idx_pics

    def distance(self,s0,s1):
        interval = u.rising_edge(s1)-u.rising_edge(s0)
        dist = interval*self.T*3e8/2
        # f = open("manim/distance.txt", "w")
        # str = str(self.fsamp) + " " + str()
        # f.write("Now the file has more content!")
        # f.close()
        return dist.round(3)

if __name__ == '__main__':

    chirp500 = chirp(15000e6,'data/200Hz_20cm.txt', 3.296e-7)
    MatrixSe, MatrixSr = chirp500.norm(0)
    signal0, signal1 = chirp500.correlate(0)
    distance = chirp500.distance(signal0,signal1)
    print(distance)
    fig, ax = plt.subplots(2)
    fig.suptitle('Démonstration Impulsion chirpée')
    ax[0].plot(MatrixSe, color="darkorange", label='émis')
    ax[0].plot(MatrixSr, label="echo 1", color='royalblue')
    ax[0].grid()
    ax[0].set_yticks([])
    ax[0].legend()
    ax[0].set(title="Représentation temporelle du signal émis et des deux échos", ylabel='Amplitude (ua)')
    ax[1].plot(signal0, color='darkorange', label='émis')
    ax[1].plot(signal1, label="echo 1", color='royalblue')
    # ax[1].plot(t[0:7500], signal1[len(t)-1:17499], label="echo 2",color='royalblue')
    ax[1].grid()
    ax[1].set(title="Représentation temporelle de l'intercorrélation des échos avec le signal émis", xlabel='t (ua)',
              ylabel='Amplitude (ua)')
    ax[1].set_yticks([])
    # ax[1].set_xticks([0,ret1,ret2])
    ax[1].legend()
    plt.show()