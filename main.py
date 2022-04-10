from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
from Detection import *
from knn_1D import *
from position import *
from radar import *
from filtrage import *
from affichage import *

if __name__ == '__main__':
    """ 1 - Pré traitement / mise en forme du signal """
    print('1')
    # Données d'entrée à fournir
    path = 'data/200Hz_10cm.txt'
    fsamp = 1500e6
    Trec = 175e-6
    nb_entrainement = 40000
    nb_garde = 10000
    taux_fa = 1e-6
    # Ouverture de fichier
    # x = np.arange(S_recu.size)
    # fe = 9 * 10 ** 9
    # Te = 1 / fe
    # t = np.arange(0, 50e-6, 6e-10)
    # chirp = signal.chirp(t, 430E6, 50e-6, 525e6)
    # print(len(chirp))
    # Ouverture, découpage du signal et mise sous forme de matrices
    # affiche_spectre(50e-6,len(chirp),40*chirp)
    S_emis, S_recu = load(path)

    print(len(S_emis))

    # Sélection d'un chirp
    tmin = 7.85e-5
    tmax = 8.15e-5
    Nmin = int(np.floor(tmin*fsamp))
    Nmax = int(np.floor(tmax*fsamp))

    MatrixSe = receivedSignalToMatrix(S_emis, fsamp, Trec)[0][Nmin:Nmax].reshape((1,-1))
    print("taille de Matrixse" + str(np.shape(MatrixSe)))
    MatrixSr = receivedSignalToMatrix(S_recu, fsamp, Trec)[0][Nmin:Nmax].reshape((1,-1))


    # plt.plot(MatrixSr)
    #(MatrixSr)
    # print(np.shape(MatrixSe))
    affiche_signal(Trec, fsamp, MatrixSe[0], MatrixSr[0])

    # signal0 = np.correlate(MatrixSr[0][0:349500], MatrixSe[0][0:349500], 'full') /fsamp
    # fig, ax = plt.subplots(2)
    # ax[0].plot(MatrixSr[0][0:349500],color='orange')
    # plt.plot(signal0, color='royalblue')
    # ax[0].plot(MatrixSe.reshape((len(MatrixSe)*len(MatrixSe[0]),1)))
    # ax[1].plot(MatrixSr.reshape((len(MatrixSr)*len(MatrixSr[0]),1)))
    #
    #
    # affiche_spectre_zoom(Trec, np.shape(MatrixSe[0])[0]/3, MatrixSe[0][0:349500])#, MatrixSr[0][0:349500])
    """ 2 - Filtrage adapté """
    print('2')
    MatrixSi = correlationMatrix(MatrixSe, MatrixSr)
    plt.plot(MatrixSi)
    plt.show()
    #
    #
    #
    # """ 3 - Detection """
    # print('3')
    # MatrixCibles = MatrixCFAR(MatrixSi, nb_entrainement, nb_garde, taux_fa)
    # plot_Cibles(list(range(len(MatrixSi[0].tolist()))), MatrixSi[0].tolist(), MatrixCibles[0].tolist())
    #
    # """ 4 - Extraction de la localisation"""
    # print('4')
    # MatrixDistances = MatrixDistance(MatrixCibles, fsamp)
    # print(MatrixDistances)

    # """ 5 - Tracking """
    # print('5')
    # jeu_test = MatrixDistances
    #
    # piste_test = [[jeu_test[0][0], 6]]
    # data_t = [[jeu_test[0][1]], [jeu_test[0][2]]]
    # data_2_t = []
    # for i in range(3, len(jeu_test[0])):
    #     data_2_t.append([jeu_test[0][i]])
    #
    # print(data_2_t)
    #
    # piste_maj_test, piste_nvx_t = algo_knn(piste_test, data_t, 1)
    #
    # for i in range(0, len(data_2_t)):
    #     piste_maj_test, piste_nvx = algo_knn(piste_maj_test, [data_2_t[i]], 3)
    #
    # print(piste_maj_test)
