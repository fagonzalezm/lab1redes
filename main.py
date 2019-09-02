import graficar as graficar
import scipy.io.wavfile as waves
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft as fou
from scipy.fftpack import ifft as iFou
from scipy.fftpack import fftfreq as fq

#1)Retorna la frecuencia de los dato por segundo y un arreglo con las amplitudes del sonido
frequency, y = waves.read('handel.wav')
#2)
period = 1.0/frequency
end = y.size*period
x = np.arange(0,end,period)
#plt.plot(y)
#plt.show()
#3)
#a)
fourier = fou(y)
frequencies = fq(len(y), period)
#b)
fourierInverse = iFou(fourier)
#c)Son los mismos graficos
print(frequency)
plt.plot(frequencies,fourier)
plt.show()

