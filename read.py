import scipy.io.wavfile as waves

def read():
    frequency, y = waves.read('handel.wav')
    print(frequency)
    print(y)
    print(type(frequency))
    print(type(y))
    print(type(y[0]))
    print(y.size)
    return frequency, y

read()