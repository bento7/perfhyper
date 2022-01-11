import numpy as np
import scipy
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt
from scipy import signal
from affichage import *
from radar import *
from filtrage import *
N = 10000
# sample spacing
T = 50.0 / 10000.0
t = np.linspace(0.0, N*T, N, endpoint=False)

ret1 = 6*np.pi
ret2 = 10*np.pi

sin= signal.chirp(t, f0=1, f1=40, t1=t[-1], method='linear')
porte = np.heaviside(t, 1) - np.heaviside(t-2*np.pi,1)
# y_f = scipy.fft.fft(sin)#*porte)
# x_f = np.linspace(0.0, 1.0/(2.0*T), N//2)
# plt.xlabel('Fréquence (Hz)')
# plt.plot(x_f, 2.0/N * np.abs(y_f[:N//2]))
# plt.grid()
# plt.title('Spectre')
# plt.show()
sin1= 0.3*signal.chirp(t-ret1, f0=1, f1=40, t1=t[-1], method='linear')
porte1 = np.heaviside(t-ret1,1) - np.heaviside(t-2*np.pi-ret1,1)


sin2= 0.1*signal.chirp(t-ret2, f0=1, f1=40, t1=t[-1], method='linear')
porte2 = np.heaviside(t-ret2,1) - np.heaviside(t-2*np.pi-ret2,1)


conv = signal.convolve(sin1*porte1,sin*porte)*T/sum(sin1*porte1)
conv1 = signal.convolve(sin2*porte2, sin*porte)*T/sum(sin2*porte2)

# plt.plot(sin*porte)
# affiche_spectre(8*np.pi, len(conv), conv)
# plt.plot(t, sin*porte)

sig0 = sin*porte
sig1 = sin1*porte1
sig2 = sin2*porte2
sig1=sig1+sig2
signal0 = np.correlate(sig1,sig0,'full')*T
signal1 = np.correlate(sig2, sig0,'full')*T
signal2 = np.correlate(sig0,sig0,'full')*T



fig, ax = plt.subplots(2)
fig.suptitle('Démonstration Impulsion chirpée')
ax[0].plot(t[0:7500],sig0[0:7500], color="darkorange", label='émis' )
ax[0].plot(t[0:7500], sig1[0:7500], label ="echo 1",color='royalblue')
# ax[0].plot(t[0:7500], sig2[0:7500], label ="echo 2",color='royalblue')
ax[0].grid()
ax[0].set_yticks([])
ax[0].set_xticks([0,ret1,ret2])
ax[0].legend()
ax[0].set(title = "Représentation temporelle du signal émis et des deux échos",ylabel='Amplitude (ua)')
ax[1].plot(t[0:7500], signal2[len(t)-1:17499], color='darkorange', label='émis')
ax[1].plot(t[0:7500], signal0[len(t)-1:17499], label="echo 1",color='royalblue')
# ax[1].plot(t[0:7500], signal1[len(t)-1:17499], label="echo 2",color='royalblue')
ax[1].grid()
ax[1].set(title = "Représentation temporelle de l'intercorrélation des échos avec le signal émis",xlabel='t (ua)',ylabel='Amplitude (ua)')
ax[1].set_yticks([])
ax[1].set_xticks([0,ret1,ret2])
ax[1].legend()
plt.show()