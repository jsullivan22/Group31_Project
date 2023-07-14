# What SignalMaker does it it generate a times series data object based on the 
# properties defined by the user like the amp, freq, length, and noise model.
import scipy.signal
import numpy as np
import matplotlib.pyplot as plt
class SignalMaker(object):
    '''
    A time series object with given properties
    '''

    def __init__(self, amp, freq, t, noise='gaussian'):
        self.amp = amp
        self.freq = freq
        self.t = t
        self.noise = noise

    def makeSignal(self):
        signal = self.amp*scipy.signal.chirp(self.t, 1, self.t[-1], self.freq)

        return signal

if __name__ == "__main__": 
    ts = np.linspace(0, 10, 100)
    test = SignalMaker(2, 100, ts).makeSignal()
    # dummy = np.ones(100)
    # plt.scatter(ts, test)
    # plt.show()

    print(test)