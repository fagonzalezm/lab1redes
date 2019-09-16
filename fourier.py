import scipy.io.wavfile as waves
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft as fft
from scipy.fftpack import ifft as ifft
from scipy.fftpack import fftfreq as freq

def a():
    frequency, y = waves.read('handel.wav')
    period = 1.0/frequency
    fourier = fft(y)
    frequencies = freq(len(y), period)
    plt.plot(frequencies,abs(fourier))
    plt.ylabel("F(w)")
    plt.xlabel("Frecuencia [Hz]")
    plt.title("Transformada de Fourier")
    plt.savefig("transformadaDeFourier.png")
    plt.show()

def b():
    frequency, y = waves.read('handel.wav')
    period = 1.0/frequency
    end = y.size*period
    x = np.arange(0,end,period)
    fourier = fft(y)
    fourierInverse = ifft(fourier)
    plt.plot(x,fourierInverse)
    plt.ylabel("Amplitud")
    plt.xlabel("Tiempo [s]")
    plt.title("Transformada de Fourier Inversa")
    plt.savefig("transformadaDeFourierInversa.png")
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
        errorAux = abs((y[i]-fourierInverse[i].real)/y[i])
        error.append(errorAux)
        i = i + 1
    fourierInverse16Bit = np.asarray(fourierInverse, dtype=np.int16)
    waves.write("out1.wav",frequency, fourierInverse16Bit)
    plt.plot(error)
    plt.ylabel("Error")
    plt.xlabel("Frecuencia")
    plt.title("Error Transformada de Fourier Inversa")
    plt.savefig("errorTransformadaDeFourierInversa.png")
    plt.show()
a()
b()
c()