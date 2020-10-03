import logging

import numpy as np

import sksdr

_log = logging.getLogger(__name__)

def test_fractional_delay0():
    delay = 0.1
    data = np.array([1, 2, 3, 4, 5], dtype=float)
    expected_data = np.array([0.9, 1.9, 2.9, 3.9, 4.9])
    vfd = sksdr.VariableFractionalDelay(10)
    out_data = vfd(data, delay)
    assert np.allclose(out_data, expected_data)

    delay = 10
    data = np.array([1, 2, 3, 4, 5], dtype=float)
    expected_data = np.array([99, 99, 99, 99, 99], dtype=float)
    vfd = sksdr.VariableFractionalDelay(10, init_state=99)
    out_data = vfd(data, delay)
    assert np.allclose(out_data, expected_data)

def test_fractional_delay1():

    # Create a delay offset object
    vfd = sksdr.VariableFractionalDelay(max_delay=5)

    # Generate random data symbols and apply QPSK modulation
    ints = np.random.randint(0, 4, 10000)
    bits = sksdr.x2binlist(ints, 2)
    psk = sksdr.PSKModulator(sksdr.QPSK, [0, 1, 3, 2], 1.0, np.pi/4)
    mod_sig = psk.modulate(bits)

    # Interpolate by 4 and filter with RRC tx filter
    interp = sksdr.FirInterpolator(4, sksdr.rrc(4, 0.5, 10))
    _, tx_sig = interp(mod_sig)

    # Apply the delay offset. Then, pass the offset signal through an AWGN channel.
    out_sig = vfd(tx_sig, 2)
    expected_sig = np.concatenate(([0, 0], tx_sig[0:-2]))
    assert np.allclose(out_sig, expected_sig)