import scipy.io.wavfile as waves

def read():
    frequency, y = waves.read('handel.wav')
    return frequency, y