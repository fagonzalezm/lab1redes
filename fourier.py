import scipy.io.wavfile as waves
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft as fft
from scipy.fftpack import ifft as ifft
from scipy.fftpack import fftfreq as freq

def a():
    frequency, y = read.read()
    period = 1.0/frequency
    fourier = fft(y)
    frequencies = freq(len(y), period)
    plt.plot(frequencies,fourier)
    plt.show()

def b():
    frequency, y = waves.read('handel.wav')
    period = 1.0/frequency
    end = y.size*period
    x = np.arange(0,end,period)
    fourier = fft(y)
    fourierInverse = ifft(fourier)
    plt.plot(x,fourierInverse)
    plt.show()

def c():
    frequency, y = waves.read('handel.wav')
    period = 1.0/frequency
    end = y.size*period
    x = np.arange(0,end,period)
    fourier = fft(y)
    fourierInverse = ifft(fourier)
    error = []
    xSize = x.size
    i = 0
    while i < xSize:
        error.append((x[i]-fourierInverse[i])/x)
        i = i + 1
    plt.plot(error)
