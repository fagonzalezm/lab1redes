import scipy.io.wavfile as waves
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft as fou
from scipy.fftpack import ifft as iFou
from scipy.fftpack import fftfreq as fq

#1)Retorna la frecuencia de los dato por segundo y un arreglo con las amplitudes del sonido
frequency, y = waves.read('handel.wav')
print(y.size)
#2)
period = 1.0/frequency
end = y.size*period
x = np.arange(0,end,period)
#plt.plot(y)
#plt.show()
#3)
#a)
#Muestra de Aplitudes de la Transformada de Fourier
fourier = fou(y)
#Muestra de frecuencias de la Transformada Discrceta de Fourier
frequencies = fq(len(y), period)
#b)
fourierInverse = iFou(fourier)
#c)Son los mismos graficos
#print(frequencies)
#print("##################################")
#print(fourier)
plt.plot(frequencies,fourier)
plt.show()
#4)
#a) La energía de la señal se concentra en las frecuencias bajas
#b)
#c)