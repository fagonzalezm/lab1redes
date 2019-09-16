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
    plt.ylabel("F(w)")
    plt.xlabel("Frecuencia [Hz]")
    plt.title("Transformada de Fourier truncada")
    plt.savefig("transformadaDeFourierTruncada.png")
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
    print(np.mean(fourier))
    mean = np.mean(fourier)*4.88
    print(mean)
    i = 0
    count = 0
    while i<xSize:
        if fourier[i] < mean:
            fourier[i] = 0
        else:
            count = count + 1
        i = i + 1
    print(count)

    fourierInverse16Bit = np.asarray(fourierInverse, dtype=np.int16)
    waves.write("out2.wav",frequency, fourierInverse16Bit)

    plt.plot(x,fourierInverse16Bit)
    plt.ylabel("Amplitud")
    plt.xlabel("Tiempo [s]")
    plt.title("Transformada de Fourier Inversa truncada")
    plt.savefig("transformadaDeFourerInversaTruncada.png")
    plt.show()

    error = []
    xSize = x.size
    i = 0
    while i < xSize:
        errorAux = abs((y[i]-fourierInverse[i].real)/y[i])
        error.append(errorAux)
        i = i + 1
    array = np.array(error)
    plt.semilogy(abs(array))
    plt.ylabel("Error")
    plt.xlabel("Frecuencia")
    plt.title("Error Transformada de Fourier truncada")
    plt.savefig("errorTransformadaDeFourierTruncada.png")
    plt.show()

a()
b()
c()
