from scipy import signal
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt
import numpy as np




def load(path):
    """
    Param :
        path : path of the file containing the data
    """
    content = np.loadtxt(path) - 127.5
    S_sent = content[:, 0]
    S_rec = content[:, 1]

    return S_sent.tolist(), S_rec.tolist()

def SignalToMatrix(signal, Fsamp, Trec):
    """
    Param :
        - signal : received signal (list of integers)
        - Fech : sampling frequency
        - Trec : recurrence period
    output : Matrix of the received signal, each column is a listening time of Trec second
    """
    signalCopy = signal.copy()
    N = int(Trec * Fsamp)
    print('N =' + str(N))
    print('len sig ' + str(len(signal)))

    Npuls = int(len(signal) // N)
    M = np.zeros((Npuls, N))

    for i in range(Npuls):
        for j in range(N):
            M[i][j] = signalCopy[i * N + j]
    return M

def rising_edge(array):
    return np.where(array > np.max(array)/3)[0][0]



