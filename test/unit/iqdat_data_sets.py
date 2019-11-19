# Copyright (C) 2019 SuperDARN
# Author: Marina Schmidt

"""
Test data sets for DmapWrite
"""
import numpy as np

from collections import OrderedDict

from pydarn import DmapScalar, DmapArray
iqdat_data = [OrderedDict([('radar.revision.major', DmapScalar(name='radar.revision.major', value=1, data_type=1, data_type_fmt='c')), ('radar.revision.minor', DmapScalar(name='radar.revision.minor', value=17, data_type=1, data_type_fmt='c')), ('origin.code', DmapScalar(name='origin.code', value=0, data_type=1, data_type_fmt='c')), ('origin.time', DmapScalar(name='origin.time', value='Wed Mar 16 19:45:04 2016', data_type=9, data_type_fmt='s')), ('origin.command', DmapScalar(name='origin.command', value='', data_type=9, data_type_fmt='s')), ('cp', DmapScalar(name='cp', value=-3560, data_type=2, data_type_fmt='h')), ('stid', DmapScalar(name='stid', value=65, data_type=2, data_type_fmt='h')), ('time.yr', DmapScalar(name='time.yr', value=2016, data_type=2, data_type_fmt='h')), ('time.mo', DmapScalar(name='time.mo', value=3, data_type=2, data_type_fmt='h')), ('time.dy', DmapScalar(name='time.dy', value=16, data_type=2, data_type_fmt='h')), ('time.hr', DmapScalar(name='time.hr', value=19, data_type=2, data_type_fmt='h')), ('time.mt', DmapScalar(name='time.mt', value=45, data_type=2, data_type_fmt='h')), ('time.sc', DmapScalar(name='time.sc', value=1, data_type=2, data_type_fmt='h')), ('time.us', DmapScalar(name='time.us', value=277995, data_type=3, data_type_fmt='i')), ('txpow', DmapScalar(name='txpow', value=9000, data_type=2, data_type_fmt='h')), ('nave', DmapScalar(name='nave', value=16, data_type=2, data_type_fmt='h')), ('atten', DmapScalar(name='atten', value=0, data_type=2, data_type_fmt='h')), ('lagfr', DmapScalar(name='lagfr', value=600, data_type=2, data_type_fmt='h')), ('smsep', DmapScalar(name='smsep', value=100, data_type=2, data_type_fmt='h')), ('ercod', DmapScalar(name='ercod', value=0, data_type=2, data_type_fmt='h')), ('stat.agc', DmapScalar(name='stat.agc', value=0, data_type=2, data_type_fmt='h')), ('stat.lopwr', DmapScalar(name='stat.lopwr', value=0, data_type=2, data_type_fmt='h')), ('noise.search', DmapScalar(name='noise.search', value=1478.2957763671875, data_type=4, data_type_fmt='f')), ('noise.mean', DmapScalar(name='noise.mean', value=456224.625, data_type=4, data_type_fmt='f')), ('channel', DmapScalar(name='channel', value=0, data_type=2, data_type_fmt='h')), ('bmnum', DmapScalar(name='bmnum', value=7, data_type=2, data_type_fmt='h')), ('bmazm', DmapScalar(name='bmazm', value=4.090000152587891, data_type=4, data_type_fmt='f')), ('scan', DmapScalar(name='scan', value=1, data_type=2, data_type_fmt='h')), ('offset', DmapScalar(name='offset', value=0, data_type=2, data_type_fmt='h')), ('rxrise', DmapScalar(name='rxrise', value=100, data_type=2, data_type_fmt='h')), ('intt.sc', DmapScalar(name='intt.sc', value=2, data_type=2, data_type_fmt='h')), ('intt.us', DmapScalar(name='intt.us', value=900000, data_type=3, data_type_fmt='i')), ('txpl', DmapScalar(name='txpl', value=100, data_type=2, data_type_fmt='h')), ('mpinc', DmapScalar(name='mpinc', value=2400, data_type=2, data_type_fmt='h')), ('mppul', DmapScalar(name='mppul', value=7, data_type=2, data_type_fmt='h')), ('mplgs', DmapScalar(name='mplgs', value=18, data_type=2, data_type_fmt='h')), ('nrang', DmapScalar(name='nrang', value=75, data_type=2, data_type_fmt='h')), ('frang', DmapScalar(name='frang', value=90, data_type=2, data_type_fmt='h')), ('rsep', DmapScalar(name='rsep', value=15, data_type=2, data_type_fmt='h')), ('xcf', DmapScalar(name='xcf', value=1, data_type=2, data_type_fmt='h')), ('tfreq', DmapScalar(name='tfreq', value=12275, data_type=2, data_type_fmt='h')), ('mxpwr', DmapScalar(name='mxpwr', value=1073741824, data_type=3, data_type_fmt='i')), ('lvmax', DmapScalar(name='lvmax', value=20000, data_type=3, data_type_fmt='i')), ('iqdata.revision.major', DmapScalar(name='iqdata.revision.major', value=0, data_type=3, data_type_fmt='i')), ('iqdata.revision.minor', DmapScalar(name='iqdata.revision.minor', value=0, data_type=3, data_type_fmt='i')), ('combf', DmapScalar(name='combf', value='$Id: multifonebm.c,v 1.0 2016/01/19 18:00:00 KKrieger Exp $', data_type=9, data_type_fmt='s')), ('seqnum', DmapScalar(name='seqnum', value=16, data_type=3, data_type_fmt='i')), ('chnnum', DmapScalar(name='chnnum', value=2, data_type=3, data_type_fmt='i')), ('smpnum', DmapScalar(name='smpnum', value=729, data_type=3, data_type_fmt='i')), ('skpnum', DmapScalar(name='skpnum', value=7, data_type=3, data_type_fmt='i')), ('ptab', DmapArray(name='ptab', value=np.array([0, 9, 12, 20, 22, 26, 27], dtype=np.int16), data_type=2, data_type_fmt='h', dimension=1, shape=[7])), ('ltab', DmapArray(name='ltab', value=np.array([0, 0, 26, 27, 20, 22, 9, 12, 22, 26, 22, 27, 20, 26, 20, 27, 12,
 20, 0, 9, 12, 22, 9, 20, 0, 12, 9, 22, 12, 26, 12, 27, 9, 26,
 9, 27, 27, 27], dtype=np.int16), data_type=2, data_type_fmt='h', dimension=2, shape=[19, 2])), ('tsc', DmapArray(name='tsc', value=np.array([1458157502, 1458157502, 1458157502, 1458157502, 1458157502,
 1458157503, 1458157503, 1458157503, 1458157503, 1458157503,
 1458157503, 1458157503, 1458157503, 1458157503, 1458157504,
 1458157504], dtype=np.int32), data_type=3, data_type_fmt='i', dimension=1, shape=[16])), ('tus', DmapArray(name='tus', value=np.array([562719, 769514, 872911, 979638, 1079705, 183702, 287083,
 390468, 496666, 597247, 703386, 804577, 907966, 1014047,
 114749, 220806], dtype=np.int32), data_type=3, data_type_fmt='i', dimension=1, shape=[16])), ('tatten', DmapArray(name='tatten', value=np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=np.int16), data_type=2, data_type_fmt='h', dimension=1, shape=[16])), ('tnoise', DmapArray(name='tnoise', value=np.array([1478.2958, 1478.2958, 1478.2958, 1478.2958, 1478.2958, 1478.2958,
 1478.2958, 1478.2958, 1478.2958, 1478.2958, 1478.2958, 1478.2958,
 1478.2958, 1478.2958, 1478.2958, 1478.2958], dtype=np.float32), data_type=4, data_type_fmt='f', dimension=1, shape=[16])), ('toff', DmapArray(name='toff', value=np.array([0, 2916, 5832, 8748, 11664, 14580, 17496, 20412, 23328,
 26244, 29160, 32076, 34992, 37908, 40824, 43740], dtype=np.int32), data_type=3, data_type_fmt='i', dimension=1, shape=[16])), ('tsze', DmapArray(name='tsze', value=np.array([2916, 2916, 2916, 2916, 2916, 2916, 2916, 2916, 2916, 2916, 2916,
 2916, 2916, 2916, 2916, 2916], dtype=np.int32), data_type=3, data_type_fmt='i', dimension=1, shape=[16])), ('data', DmapArray(name='data', value=np.array([-5, -11, 1, -25, -11, 54], dtype=np.int16), data_type=2, data_type_fmt='h', dimension=1, shape=[6]))]), OrderedDict([('radar.revision.major', DmapScalar(name='radar.revision.major', value=1, data_type=1, data_type_fmt='c')), ('radar.revision.minor', DmapScalar(name='radar.revision.minor', value=17, data_type=1, data_type_fmt='c')), ('origin.code', DmapScalar(name='origin.code', value=0, data_type=1, data_type_fmt='c')), ('origin.time', DmapScalar(name='origin.time', value='Wed Mar 16 19:48:02 2016', data_type=9, data_type_fmt='s')), ('origin.command', DmapScalar(name='origin.command', value='', data_type=9, data_type_fmt='s')), ('cp', DmapScalar(name='cp', value=-3560, data_type=2, data_type_fmt='h')), ('stid', DmapScalar(name='stid', value=65, data_type=2, data_type_fmt='h')), ('time.yr', DmapScalar(name='time.yr', value=2016, data_type=2, data_type_fmt='h')), ('time.mo', DmapScalar(name='time.mo', value=3, data_type=2, data_type_fmt='h')), ('time.dy', DmapScalar(name='time.dy', value=16, data_type=2, data_type_fmt='h')), ('time.hr', DmapScalar(name='time.hr', value=19, data_type=2, data_type_fmt='h')), ('time.mt', DmapScalar(name='time.mt', value=48, data_type=2, data_type_fmt='h')), ('time.sc', DmapScalar(name='time.sc', value=0, data_type=2, data_type_fmt='h')), ('time.us', DmapScalar(name='time.us', value=22004, data_type=3, data_type_fmt='i')), ('txpow', DmapScalar(name='txpow', value=9000, data_type=2, data_type_fmt='h')), ('nave', DmapScalar(name='nave', value=26, data_type=2, data_type_fmt='h')), ('atten', DmapScalar(name='atten', value=0, data_type=2, data_type_fmt='h')), ('lagfr', DmapScalar(name='lagfr', value=600, data_type=2, data_type_fmt='h')), ('smsep', DmapScalar(name='smsep', value=100, data_type=2, data_type_fmt='h')), ('ercod', DmapScalar(name='ercod', value=0, data_type=2, data_type_fmt='h')), ('stat.agc', DmapScalar(name='stat.agc', value=0, data_type=2, data_type_fmt='h')), ('stat.lopwr', DmapScalar(name='stat.lopwr', value=0, data_type=2, data_type_fmt='h')), ('noise.search', DmapScalar(name='noise.search', value=2762.113037109375, data_type=4, data_type_fmt='f')), ('noise.mean', DmapScalar(name='noise.mean', value=456916.71875, data_type=4, data_type_fmt='f')), ('channel', DmapScalar(name='channel', value=0, data_type=2, data_type_fmt='h')), ('bmnum', DmapScalar(name='bmnum', value=7, data_type=2, data_type_fmt='h')), ('bmazm', DmapScalar(name='bmazm', value=4.090000152587891, data_type=4, data_type_fmt='f')), ('scan', DmapScalar(name='scan', value=1, data_type=2, data_type_fmt='h')), ('offset', DmapScalar(name='offset', value=0, data_type=2, data_type_fmt='h')), ('rxrise', DmapScalar(name='rxrise', value=100, data_type=2, data_type_fmt='h')), ('intt.sc', DmapScalar(name='intt.sc', value=2, data_type=2, data_type_fmt='h')), ('intt.us', DmapScalar(name='intt.us', value=900000, data_type=3, data_type_fmt='i')), ('txpl', DmapScalar(name='txpl', value=100, data_type=2, data_type_fmt='h')), ('mpinc', DmapScalar(name='mpinc', value=2400, data_type=2, data_type_fmt='h')), ('mppul', DmapScalar(name='mppul', value=7, data_type=2, data_type_fmt='h')), ('mplgs', DmapScalar(name='mplgs', value=18, data_type=2, data_type_fmt='h')), ('nrang', DmapScalar(name='nrang', value=75, data_type=2, data_type_fmt='h')), ('frang', DmapScalar(name='frang', value=90, data_type=2, data_type_fmt='h')), ('rsep', DmapScalar(name='rsep', value=15, data_type=2, data_type_fmt='h')), ('xcf', DmapScalar(name='xcf', value=1, data_type=2, data_type_fmt='h')), ('tfreq', DmapScalar(name='tfreq', value=12088, data_type=2, data_type_fmt='h')), ('mxpwr', DmapScalar(name='mxpwr', value=1073741824, data_type=3, data_type_fmt='i')), ('lvmax', DmapScalar(name='lvmax', value=20000, data_type=3, data_type_fmt='i')), ('iqdata.revision.major', DmapScalar(name='iqdata.revision.major', value=0, data_type=3, data_type_fmt='i')), ('iqdata.revision.minor', DmapScalar(name='iqdata.revision.minor', value=0, data_type=3, data_type_fmt='i')), ('combf', DmapScalar(name='combf', value='$Id: multifonebm.c,v 1.0 2016/01/19 18:00:00 KKrieger Exp $', data_type=9, data_type_fmt='s')), ('seqnum', DmapScalar(name='seqnum', value=26, data_type=3, data_type_fmt='i')), ('chnnum', DmapScalar(name='chnnum', value=2, data_type=3, data_type_fmt='i')), ('smpnum', DmapScalar(name='smpnum', value=729, data_type=3, data_type_fmt='i')), ('skpnum', DmapScalar(name='skpnum', value=7, data_type=3, data_type_fmt='i')), ('ptab', DmapArray(name='ptab', value=np.array([0, 9, 12, 20, 22, 26, 27], dtype=np.int16), data_type=2, data_type_fmt='h', dimension=1, shape=[7])), ('ltab', DmapArray(name='ltab', value=np.array([0, 0, 26, 27, 20, 22, 9, 12, 22, 26, 22, 27, 20, 26, 20, 27, 12,
 20, 0, 9, 12, 22, 9, 20, 0, 12, 9, 22, 12, 26, 12, 27, 9, 26,
 9, 27, 27, 27], dtype=np.int16), data_type=2, data_type_fmt='h', dimension=2, shape=[19, 2])), ('tsc', DmapArray(name='tsc', value=np.array([1458157680, 1458157680, 1458157680, 1458157680, 1458157680,
 1458157680, 1458157680, 1458157681, 1458157681, 1458157681,
 1458157681, 1458157681, 1458157681, 1458157681, 1458157681,
 1458157681, 1458157681, 1458157682, 1458157682, 1458157682,
 1458157682, 1458157682, 1458157682, 1458157682, 1458157682,
 1458157682], dtype=np.int32), data_type=3, data_type_fmt='i', dimension=1, shape=[26])), ('tus', DmapArray(name='tus', value=np.array([318710, 530499, 634147, 737627, 837570, 940892, 1047153,
 151597, 255467, 356013, 459377, 565472, 669910, 773803,
 874486, 977862, 1083894, 188324, 292222, 392966, 496872,
 602347, 706770, 810670, 911448, 1015352], dtype=np.int32), data_type=3, data_type_fmt='i', dimension=1, shape=[26])), ('tatten', DmapArray(name='tatten', value=np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0], dtype=np.int16), data_type=2, data_type_fmt='h', dimension=1, shape=[26])), ('tnoise', DmapArray(name='tnoise', value=np.array([2762.113, 2762.113, 2762.113, 2762.113, 2762.113, 2762.113,
 2762.113, 2762.113, 2762.113, 2762.113, 2762.113, 2762.113,
 2762.113, 2762.113, 2762.113, 2762.113, 2762.113, 2762.113,
 2762.113, 2762.113, 2762.113, 2762.113, 2762.113, 2762.113,
 2762.113, 2762.113], dtype=np.float32), data_type=4, data_type_fmt='f', dimension=1, shape=[26])), ('toff', DmapArray(name='toff', value=np.array([0, 2916, 5832, 8748, 11664, 14580, 17496, 20412, 23328,
 26244, 29160, 32076, 34992, 37908, 40824, 43740, 46656, 49572,
 52488, 55404, 58320, 61236, 64152, 67068, 69984, 72900],
 dtype=np.int32), data_type=3, data_type_fmt='i', dimension=1, shape=[26])), ('tsze', DmapArray(name='tsze', value=np.array([2916, 2916, 2916, 2916, 2916, 2916, 2916, 2916, 2916, 2916, 2916,
 2916, 2916, 2916, 2916, 2916, 2916, 2916, 2916, 2916, 2916, 2916,
 2916, 2916, 2916, 2916], dtype=np.int32), data_type=3, data_type_fmt='i', dimension=1, shape=[26])), ('data', DmapArray(name='data', value=np.array([-85, 1, 149, -5, -10, -7], dtype=np.int16), data_type=2, data_type_fmt='h', dimension=1, shape=[6]))]), OrderedDict([('radar.revision.major', DmapScalar(name='radar.revision.major', value=1, data_type=1, data_type_fmt='c')), ('radar.revision.minor', DmapScalar(name='radar.revision.minor', value=17, data_type=1, data_type_fmt='c')), ('origin.code', DmapScalar(name='origin.code', value=0, data_type=1, data_type_fmt='c')), ('origin.time', DmapScalar(name='origin.time', value='Wed Mar 16 19:49:56 2016', data_type=9, data_type_fmt='s')), ('origin.command', DmapScalar(name='origin.command', value='', data_type=9, data_type_fmt='s')), ('cp', DmapScalar(name='cp', value=-3560, data_type=2, data_type_fmt='h')), ('stid', DmapScalar(name='stid', value=65, data_type=2, data_type_fmt='h')), ('time.yr', DmapScalar(name='time.yr', value=2016, data_type=2, data_type_fmt='h')), ('time.mo', DmapScalar(name='time.mo', value=3, data_type=2, data_type_fmt='h')), ('time.dy', DmapScalar(name='time.dy', value=16, data_type=2, data_type_fmt='h')), ('time.hr', DmapScalar(name='time.hr', value=19, data_type=2, data_type_fmt='h')), ('time.mt', DmapScalar(name='time.mt', value=49, data_type=2, data_type_fmt='h')), ('time.sc', DmapScalar(name='time.sc', value=53, data_type=2, data_type_fmt='h')), ('time.us', DmapScalar(name='time.us', value=231589, data_type=3, data_type_fmt='i')), ('txpow', DmapScalar(name='txpow', value=9000, data_type=2, data_type_fmt='h')), ('nave', DmapScalar(name='nave', value=26, data_type=2, data_type_fmt='h')), ('atten', DmapScalar(name='atten', value=0, data_type=2, data_type_fmt='h')), ('lagfr', DmapScalar(name='lagfr', value=600, data_type=2, data_type_fmt='h')), ('smsep', DmapScalar(name='smsep', value=100, data_type=2, data_type_fmt='h')), ('ercod', DmapScalar(name='ercod', value=0, data_type=2, data_type_fmt='h')), ('stat.agc', DmapScalar(name='stat.agc', value=0, data_type=2, data_type_fmt='h')), ('stat.lopwr', DmapScalar(name='stat.lopwr', value=0, data_type=2, data_type_fmt='h')), ('noise.search', DmapScalar(name='noise.search', value=994.9771118164062, data_type=4, data_type_fmt='f')), ('noise.mean', DmapScalar(name='noise.mean', value=456085.6875, data_type=4, data_type_fmt='f')), ('channel', DmapScalar(name='channel', value=0, data_type=2, data_type_fmt='h')), ('bmnum', DmapScalar(name='bmnum', value=7, data_type=2, data_type_fmt='h')), ('bmazm', DmapScalar(name='bmazm', value=4.090000152587891, data_type=4, data_type_fmt='f')), ('scan', DmapScalar(name='scan', value=0, data_type=2, data_type_fmt='h')), ('offset', DmapScalar(name='offset', value=0, data_type=2, data_type_fmt='h')), ('rxrise', DmapScalar(name='rxrise', value=100, data_type=2, data_type_fmt='h')), ('intt.sc', DmapScalar(name='intt.sc', value=2, data_type=2, data_type_fmt='h')), ('intt.us', DmapScalar(name='intt.us', value=900000, data_type=3, data_type_fmt='i')), ('txpl', DmapScalar(name='txpl', value=100, data_type=2, data_type_fmt='h')), ('mpinc', DmapScalar(name='mpinc', value=2400, data_type=2, data_type_fmt='h')), ('mppul', DmapScalar(name='mppul', value=7, data_type=2, data_type_fmt='h')), ('mplgs', DmapScalar(name='mplgs', value=18, data_type=2, data_type_fmt='h')), ('nrang', DmapScalar(name='nrang', value=75, data_type=2, data_type_fmt='h')), ('frang', DmapScalar(name='frang', value=90, data_type=2, data_type_fmt='h')), ('rsep', DmapScalar(name='rsep', value=15, data_type=2, data_type_fmt='h')), ('xcf', DmapScalar(name='xcf', value=1, data_type=2, data_type_fmt='h')), ('tfreq', DmapScalar(name='tfreq', value=12088, data_type=2, data_type_fmt='h')), ('mxpwr', DmapScalar(name='mxpwr', value=1073741824, data_type=3, data_type_fmt='i')), ('lvmax', DmapScalar(name='lvmax', value=20000, data_type=3, data_type_fmt='i')), ('iqdata.revision.major', DmapScalar(name='iqdata.revision.major', value=0, data_type=3, data_type_fmt='i')), ('iqdata.revision.minor', DmapScalar(name='iqdata.revision.minor', value=0, data_type=3, data_type_fmt='i')), ('combf', DmapScalar(name='combf', value='$Id: multifonebm.c,v 1.0 2016/01/19 18:00:00 KKrieger Exp $', data_type=9, data_type_fmt='s')), ('seqnum', DmapScalar(name='seqnum', value=26, data_type=3, data_type_fmt='i')), ('chnnum', DmapScalar(name='chnnum', value=2, data_type=3, data_type_fmt='i')), ('smpnum', DmapScalar(name='smpnum', value=729, data_type=3, data_type_fmt='i')), ('skpnum', DmapScalar(name='skpnum', value=7, data_type=3, data_type_fmt='i')), ('ptab', DmapArray(name='ptab', value=np.array([0, 9, 12, 20, 22, 26, 27], dtype=np.int16), data_type=2, data_type_fmt='h', dimension=1, shape=[7])), ('ltab', DmapArray(name='ltab', value=np.array([0, 0, 26, 27, 20, 22, 9, 12, 22, 26, 22, 27, 20, 26, 20, 27, 12,
 20, 0, 9, 12, 22, 9, 20, 0, 12, 9, 22, 12, 26, 12, 27, 9, 26,
 9, 27, 27, 27], dtype=np.int16), data_type=2, data_type_fmt='h', dimension=2, shape=[19, 2])), ('tsc', DmapArray(name='tsc', value=np.array([1458157793, 1458157793, 1458157793, 1458157793, 1458157793,
 1458157794, 1458157794, 1458157794, 1458157794, 1458157794,
 1458157794, 1458157794, 1458157794, 1458157794, 1458157794,
 1458157795, 1458157795, 1458157795, 1458157795, 1458157795,
 1458157795, 1458157795, 1458157795, 1458157795, 1458157796,
 1458157796], dtype=np.int32), data_type=3, data_type_fmt='i', dimension=1, shape=[26])), ('tus', DmapArray(name='tus', value=np.array([531291, 736088, 841483, 947545, 1052024, 155871, 255655,
 360183, 466363, 570260, 674157, 774239, 878703, 984771,
 1088673, 189378, 292761, 398790, 503222, 607125, 707880,
 811265, 917263, 1021688, 125590, 226375], dtype=np.int32), data_type=3, data_type_fmt='i', dimension=1, shape=[26])), ('tatten', DmapArray(name='tatten', value=np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0], dtype=np.int16), data_type=2, data_type_fmt='h', dimension=1, shape=[26])), ('tnoise', DmapArray(name='tnoise', value=np.array([994.9771, 994.9771, 994.9771, 994.9771, 994.9771, 994.9771,
 994.9771, 994.9771, 994.9771, 994.9771, 994.9771, 994.9771,
 994.9771, 994.9771, 994.9771, 994.9771, 994.9771, 994.9771,
 994.9771, 994.9771, 994.9771, 994.9771, 994.9771, 994.9771,
 994.9771, 994.9771], dtype=np.float32), data_type=4, data_type_fmt='f', dimension=1, shape=[26])), ('toff', DmapArray(name='toff', value=np.array([0, 2916, 5832, 8748, 11664, 14580, 17496, 20412, 23328,
 26244, 29160, 32076, 34992, 37908, 40824, 43740, 46656, 49572,
 52488, 55404, 58320, 61236, 64152, 67068, 69984, 72900],
 dtype=np.int32), data_type=3, data_type_fmt='i', dimension=1, shape=[26])), ('tsze', DmapArray(name='tsze', value=np.array([2916, 2916, 2916, 2916, 2916, 2916, 2916, 2916, 2916, 2916, 2916,
 2916, 2916, 2916, 2916, 2916, 2916, 2916, 2916, 2916, 2916, 2916,
 2916, 2916, 2916, 2916], dtype=np.int32), data_type=3, data_type_fmt='i', dimension=1, shape=[26])), ('data', DmapArray(name='data', value=np.array([-15, -22, -2, 3, 9, 8], dtype=np.int16), data_type=2, data_type_fmt='h', dimension=1, shape=[6]))])]