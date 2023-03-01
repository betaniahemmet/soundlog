import scipy.io.wavfile as wavfile
import numpy as np
import matplotlib.pyplot as plt
from audiolog import record
#rate, data = wavfile.read('FILE.wav')
#t = np.arange(len(data[:,0]))*1.0/rate
#plt.plot(t, data[:,0])
#plt.show()

def main():
    i = 50
    maxes = []
    while i>1:
        record()
        rate, data = wavfile.read('FILE.wav')
        maxes.append(data.max())
        print(maxes)
        print(len(maxes))

if __name__ == "__main__":
    main()
