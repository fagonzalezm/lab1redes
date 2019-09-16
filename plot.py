import numpy as np
import matplotlib.pyplot as plt
import read as read

def plot():
    frequency, y = read.read()
    period = 1.0/frequency
    end = y.size*period
    x = np.arange(0,end,period)
    plt.plot(x,y)
    plt.ylabel("Amplitud")
    plt.xlabel("Tiempo [s]")
    plt.title("Señal de audio")
    plt.show()
    
plot()