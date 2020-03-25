"""
Test data sets for DmapWrite
"""
from numpy import array, int8, int16, float32


rawacf_dict_data = [{'radar.revision.major': int8(1),
                     'radar.revision.minor': int8(18),
                     'origin.code': int8(0),
                     'origin.time': 'Mon Apr 18: 01: 03 2017',
                     'origin.command': 'twofsound -fast -xcf 1 -p7',
                     'cp': int16(3505),
                     'stid': int16(5),
                     'time.yr': int16(2017),
                     'time.mo': int16(4),
                     'time.dy': int16(10),
                     'time.hr': int16(18),
                     'time.mt': int16(1),
                     'time.sc': int16(0),
                     'time.us': 35565,
                     'txpow': int16(9000),
                     'nave': int16(32),
                     'atten': int16(0),
                     'lagfr': int16(1200),
                     'smsep': int16(300),
                     'ercod': int16(0),
                     'stat.agc': int16(0),
                     'stat.lopwr': int16(0),
                     'noise.search': 27.822126388549805,
                     'noise.mean': 505125.4375,
                     'channel': int16(2),
                     'bmnum': int16(0),
                     'bmazm': -1.2000000476837158,
                     'scan': int16(1),
                     'offset': int16(0),
                     'rxrise': int16(100),
                     'intt.sc': int16(3),
                     'intt.us': 500000,
                     'txpl': int16(300),
                     'mpinc': int16(2400),
                     'mppul': int16(7),
                     'mplgs': int16(18),
                     'nrang': int16(75),
                     'frang': int16(180),
                     'rsep': int16(45),
                     'xcf': int16(1),
                     'tfreq': int16(13078),
                     'mxpwr': 1073741824,
                     'lvmax': 20000,
                     'rawacf.revision.major': 0,
                     'rawacf.revision.minor': 0,
                     'combf': '$Id: twofsound.c,v 1.0016/11/08 20:00:00'
                     ' KKrieger Exp $',
                     'thr': 0.0,
                     'ptab': array([0,  9, 12, 20, 22, 26, 27], dtype=int16),
                     'ltab': array([0,  0, 26, 27, 20, 22, 12, 22, 26,
                                    22, 27, 20, 26, 20, 27, 12, 20,
                                    0, 9, 12, 22,  9, 20, 0, 12,  9,
                                    22, 12, 26, 12, 27, 9, 26, 27, 27, 27],
                                   dtype=int16),
                     'slist': array([0,  2, 3, 4, 5, 6, 7, 0, 11, 12, 13,
                                     14, 15, 16, 17, 18, 19, 20, 21, 22,
                                     23, 24, 25, 26, 27, 28, 29, 30, 31,
                                     32, 33, 34, 35, 36, 37, 38, 39, 40,
                                     41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
                                     51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
                                     61, 62, 63, 64, 65, 66, 67,
                                     68, 69, 70, 71, 72, 73, 74], dtype=int16),
                     'pwr0': array([98.4375, 235.3125, 160.5, 59.1875,
                                    43.65625, 65.40625, 62.03125, 46.25,
                                    72.84375, 60.0625, 47.40625, 61.0625,
                                    62.5625, 60.46875, 59.53125, 42.84375,
                                    39.78125, 40.9375, 51.6875, 55.125,
                                    37.03125, 56.15625, 51.71875, 50.40625,
                                    58.46875, 59.21875, 61.90625, 61.71875,
                                    53.84375, 51.5625, 55.4375, 38.8125,
                                    93.09375, 279.8125, 267.59375, 417.875,
                                    1232.4062, 281.125, 126.3125, 60.65625,
                                    62.12, 118.5, 351.5625, 778.96875,
                                    126.53125, 151.46875,  82.21875, 86.625,
                                    61.4375, 69, 92.71875, 61.15625,
                                    72.0625, 77.84375, 49.84375, 69.28125,
                                    61.15625, 72.125, 69.125, 66.8125,
                                    59.625, 71.21875, 62.34375, 57.28125,
                                    54.96875, 52.65625, 61.84375, 56.34375,
                                    75.875, 97.25, 80.125, 44.5625,
                                    52.53125, 81.40625, 86.03125],
                                   dtype=float32),
                     'acfd': array([98.4375, 0, 26.59375, -8.5,
                                    28.90625, -3.5625], dtype=float32),
                     'xcfd': array([-11., 14.875, 0.84375, 2.375,
                                    72.21875, 4.21875], dtype=float32)}]
