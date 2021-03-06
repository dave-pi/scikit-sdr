#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2020 gr-grsksdr author.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#
import logging

import numpy as np
import sksdr
from gnuradio import gr

_log = logging.getLogger(__name__)
#_log.setLevel(logging.DEBUG)

class psk_demod(gr.sync_block):
    """
    docstring for block psk_demod
    """
    def __init__(self, modulation, labels, amplitude, phase_offset):
        mod = eval(modulation)
        gr.sync_block.__init__(self,
                                 name='psk_demod',
                                 in_sig=[np.complex64],
                                 out_sig=[np.uint8])
        mod = eval(modulation)
        self.psk = sksdr.PSKModulator.from_modulation(mod, labels, amplitude, phase_offset)
        self.symbols_per_byte = 8 // mod.bits_per_symbol

    # def forecast(self, noutput_items, ninput_items_required):
    #     for i in range(len(ninput_items_required)):
    #         ninput_items_required[i] = noutput_items * self.symbols_per_byte

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        nout = len(out)
        # print(len(in0), len(out), len(out) // self.symbols_per_byte)
        self.psk.demodulate(in0, out)
        # self.consume(0, nout * self.symbols_per_byte)
        return nout
