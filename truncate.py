import scipy.io.wavfile as waves
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft as fft
from scipy.fftpack import ifft as ifft
from scipy.fftpack import fftfreq as freq


def a():
    frequency, y = waves.read('handel.wav')
    period = 1.0/frequency
    end = y.size*period
    x = np.arange(0,end,period)
    fourier = abs(fft(y))
    frequencies = freq(len(y), period)
    xSize = x.size
    mean = 4.88*np.mean(fourier)
    print(mean)

def b():
    frequency, y = waves.read('handel.wav')
    period = 1.0/frequency
    end = y.size*period
    x = np.arange(0,end,period)
    fourier = abs(fft(y))
    frequencies = freq(len(y), period)
    xSize = x.size
    mean = 4.88*np.mean(fourier)
    i = 0
    while i<xSize:
        if fourier[i] < mean:
            fourier[i] = 0
        i = i + 1
    counter = 0
    for data in fourier:
        if data != 0:
            counter = counter + 1
    print(xSize/2)
    print(counter)
    plt.plot(frequencies, fourier)  
    plt.show()

def c():
    frequency, y = waves.read('handel.wav')
    period = 1.0/frequency
    end = y.size*period
    x = np.arange(0,end,period)
    fourier = abs(fft(y))
    fourierInverse = ifft(fourier)
    frequencies = freq(len(y), period)
    xSize = x.size
    mean = np.mean(fourier)*4.88
    i = 0
    while i<xSize:
        if fourier[i] < mean:
            fourier[i] = 0
        i = i + 1

    fourierInverse16Bit = np.asarray(fourierInverse, dtype=np.int16)
    waves.write("outTruncated3.wav",frequency, fourierInverse16Bit)

    error = []
    xSize = x.size
    i = 0
    while i < xSize:
        errorAux = abs((y[i]-fourierInverse[i].real)/y[i])
        error.append(errorAux)
        i = i + 1
    plt.plot(error)
    plt.show()
    
c()
