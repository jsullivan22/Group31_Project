import pytest
from data_generation import *

def test_generated_signal(amp, t, freq):
    '''
    Tests if the generated signal is in the form of a numpy array.
    '''

    # step 1 generate a test signal
    ts = np.linspace(0, t, 100)
    test = SignalMaker(amp, freq, ts).makeSignal() 
    assert type(test) == np.ndarray

test_generated_signal(2, 10, 100)