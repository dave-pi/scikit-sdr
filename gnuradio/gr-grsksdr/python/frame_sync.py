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
from logging import DEBUG

import numpy as np
import sksdr
from gnuradio import gr

_log = logging.getLogger(__name__)
#_log.setLevel(logging.DEBUG)

class frame_sync(gr.basic_block):
    """
    docstring for block frame_sync
    """
    def __init__(self, preamble, det_thr, frame_size):
        self.frame_size = frame_size
        gr.basic_block.__init__(self,
                                name='frame_sync',
                                in_sig=[np.complex64],
                                out_sig=[np.complex64])
        self.frame_sync = sksdr.PreambleSync(preamble, det_thr, frame_size)
        self.set_output_multiple(self.frame_size)

    def forecast(self, noutput_items, ninput_items_required):
        # setup size of input_items[i] for work call
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = noutput_items

    def general_work(self, input_items, output_items):
        in0 = input_items[0]
        out0 = output_items[0]
        nin0 = len(in0)
        nout0 = len(out0)
        _log.debug('len in0/out0: %d/%d', nin0, nout0)
        nret = 0
        nin = int(nin0 / self.frame_size) * self.frame_size
        for i in range(0, nin, self.frame_size):
            valid = self.frame_sync(in0[i : i + self.frame_size], out0[nret : nret + self.frame_size])
            if valid:
                nret += self.frame_size
                if nret == nout0:
                    break

        self.consume(0, i + self.frame_size)
        return nret
