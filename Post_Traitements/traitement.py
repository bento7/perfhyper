import numpy as np
import matplotlib.pyplot as plt
from affichage import *
from radar import *
from filtrage import *
""" 1 - Pré traitement / mise en forme du signal """
print('1')
# Données d'entrée à fournir
path = '../data/500Hz_5cm.txt'
fsamp = 15000e6
T=1/fsamp
Trec = 3.296e-7
nb_entrainement = 40000
nb_garde = 10000
taux_fa = 1e-6

S_emis, S_recu = load(path)

print(len(S_emis))

# Sélection d'un chirp
tmin = 8.35e-6
tmax = 9.00e-6
Nmin = int(np.floor(tmin*fsamp))
Nmax = int(np.floor(tmax*fsamp))

MatrixSe = receivedSignalToMatrix(S_emis, fsamp, Trec)[0][:].reshape((-1,1))
MatrixSe /= max(MatrixSe)
print("taille de Matrixse" + str(np.shape(MatrixSe)))
MatrixSr = receivedSignalToMatrix(S_recu, fsamp, Trec)[0][:].reshape((-1,1))
MatrixSr /= max(MatrixSr)
print(np.shape(MatrixSe[:, 0]))

# conv = signal.convolve(MatrixSe,MatrixSr)*T#/max(MatrixSe)

# plt.plot(sin*porte)
# affiche_spectre(8*np.pi, len(conv), conv)
# plt.plot(t, sin*porte)


signal0 = np.correlate(MatrixSe[:, 0],MatrixSe[:, 0],'full')*T
signal1 = np.correlate(MatrixSr[:, 0], MatrixSe[:, 0],'full')*T
# signal2 = np.correlate(MatrixSr,MatrixSr,'full')*T



fig, ax = plt.subplots(2)
fig.suptitle('Démonstration Impulsion chirpée')
ax[0].plot(MatrixSe, color="darkorange", label='émis' )
ax[0].plot(MatrixSr, label ="echo 1",color='royalblue')
# ax[0].plot(t[0:7500], sig2[0:7500], label ="echo 2",color='royalblue')
ax[0].grid()
ax[0].set_yticks([])
# ax[0].set_xticks([0,ret1,ret2])
ax[0].legend()
ax[0].set(title = "Représentation temporelle du signal émis et des deux échos",ylabel='Amplitude (ua)')
ax[1].plot(signal0, color='darkorange', label='émis')
ax[1].plot(signal1, label="echo 1",color='royalblue')
# ax[1].plot(t[0:7500], signal1[len(t)-1:17499], label="echo 2",color='royalblue')
ax[1].grid()
ax[1].set(title = "Représentation temporelle de l'intercorrélation des échos avec le signal émis",xlabel='t (ua)',ylabel='Amplitude (ua)')
ax[1].set_yticks([])
# ax[1].set_xticks([0,ret1,ret2])
ax[1].legend()
plt.show()