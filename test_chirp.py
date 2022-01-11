import numpy as np
import matplotlib.pyplot as plt
from affichage import *
from scipy import signal

fstart = 430E6
BW = 100E6
tau = 1E-6

t = np.arange(0, 1E-6, 1E-12)

def chirp(t):
    return np.cos(2*np.pi*(fstart + BW*t/tau)*t)

t = np.linspace(0, 10, 1500)
w = signal.chirp(t, f0=0, f1=4, t1=10, method='linear')
f = 4 * t
plt.title("Linear Chirp")

plt.subplot(111)
plt.plot(t, f)
plt.grid()
plt.ylabel('f (Hz)')
plt.xlabel('t (sec)')
plt.subplot(112)
affiche_spectre(1E-6, len(t), c)

plt.show()
