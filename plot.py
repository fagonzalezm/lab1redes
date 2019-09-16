import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves

def plot():
    frequency, y = waves.read('handel.wav')
    period = 1.0/frequency
    print(period)
    end = y.size*period
    print(end)
    x = np.arange(0,end,period)
    plt.plot(x,y)
    plt.ylabel("Amplitud")
    plt.xlabel("Tiempo [s]")
    plt.title("Señal de audio")
    plt.savefig("senialDeAudio.png")
    plt.show()
    
plot()