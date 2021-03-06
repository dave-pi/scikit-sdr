"""
Sequences.
"""
import logging

_log = logging.getLogger(__name__)

UNIPOLAR_BARKER_SEQ = {
        2: [0, 1],
        3: [1, 1, 0],
        4: [1, 1, 0, 1],
        5: [1, 1, 1, 0, 1],
        7: [1, 1, 1, 0, 0, 1, 0],
        11: [1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0],
        13: [1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1],
    }
"""
Barker sequences.
"""
