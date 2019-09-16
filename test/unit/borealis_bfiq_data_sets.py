"""
Test data sets for Borealis Bfiq.
"""

from collections import OrderedDict
from numpy import array, int16, int64, uint32, float32, float64, \
                  zeros, str_, bool_, complex64

borealis_site_bfiq_data = OrderedDict([(1558583991060, {
    "borealis_git_hash": str_('v0.2-61-gc13ab34'), 
    "experiment_id": int64(100000000),
    "experiment_name": str_('TestScheme9ACFs'), 
    "experiment_comment": str_(''), 
    "num_slices": int64(1), 
    "slice_comment": str_(''), 
    "station": str_('sas'),
    "num_sequences": int64(29), 
    "pulse_phase_offset": array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]).astype(float32),
    "range_sep": float32(44.96887), 
    "first_range_rtt": float32(1200.8307), 
    "first_range": float32(180.0), 
    "rx_sample_rate": float64(3333.3333333333335),
    "scan_start_marker": bool_(True), 
    "int_time": float32(3.000395), 
    "tx_pulse_len": uint32(300), 
    "tau_spacing": uint32(2400), 
    "main_antenna_count": uint32(16), 
    "intf_antenna_count": uint32(4), 
    "freq": uint32(10500), 
    "samples_data_type": str_('complex float'), 
    "num_samps": uint32(297),
    "num_ranges": uint32(75),
    "pulses": array([0, 9, 12, 20, 22, 26, 27]).astype(uint32), 
    "lags": array([[ 0,  0],
                    [26, 27],
                    [20, 22],
                    [9, 12],
                    [22, 26],
                    [22, 27],
                    [20, 26],
                    [20, 27],
                    [12, 20],
                    [0, 9],
                    [12, 22],
                    [9, 20],
                    [0, 12],
                    [9, 22],
                    [12, 26],
                    [12, 27],
                    [9, 26],
                    [9, 27],
                    [0, 20],
                    [0, 22],
                    [0, 26],
                    [0, 27],
                    [27, 27]]).astype(uint32),
    "blanked_samples": array([0, 72, 96, 160, 176, 208, 216]).astype(uint32), 
    "sqn_timestamps": array([1.55858399e+09, 1.55858399e+09,
    1.55858399e+09, 1.55858399e+09, 1.55858399e+09, 1.55858399e+09, 
    1.55858399e+09, 1.55858399e+09, 1.55858399e+09, 1.55858399e+09, 
    1.55858399e+09, 1.55858399e+09, 1.55858399e+09, 1.55858399e+09, 
    1.55858399e+09, 1.55858399e+09, 1.55858399e+09, 1.55858399e+09, 
    1.55858399e+09, 1.55858399e+09, 1.55858399e+09, 1.55858399e+09, 
    1.55858399e+09, 1.55858399e+09, 1.55858399e+09, 1.55858399e+09, 
    1.55858399e+09, 1.55858399e+09, 1.55858399e+09]), 
    "beam_nums": array([0]).astype(uint32), 
    "beam_azms": array([0.0]), 
    "data_descriptors": array(['num_antenna_arrays', 'num_sequences', 
                                'num_beams', 'num_samps']), 
    "data_dimensions": array([2, 29, 1, 297]).astype(uint32), 
    "antenna_arrays_order": array(['main', 'intf']),
    "noise_at_freq": array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 
                             0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 
                             0., 0., 0., 0., 0., 0., 0.]), 
    "data_normalization_factor": float64(9999999.999999996),
    "data": zeros(17226).astype(complex64)
    }), 
    (1558583994062, {
    "borealis_git_hash": str_('v0.2-61-gc13ab34'), 
    "experiment_id": int64(100000000),
    "experiment_name": str_('TestScheme9ACFs'), 
    "experiment_comment": str_(''), 
    "num_slices": int64(1), 
    "slice_comment": str_(''), 
    "station": str_('sas'),
    "num_sequences": int64(29), 
    "pulse_phase_offset": array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]).astype(float32),
    "range_sep": float32(44.96887), 
    "first_range_rtt": float32(1200.8307), 
    "first_range": float32(180.0), 
    "rx_sample_rate": float64(3333.3333333333335),
    "scan_start_marker": bool_(True), 
    "int_time": float32(3.090798), 
    "tx_pulse_len": uint32(300), 
    "tau_spacing": uint32(2400), 
    "main_antenna_count": uint32(16), 
    "intf_antenna_count": uint32(4), 
    "freq": uint32(10500), 
    "samples_data_type": str_('complex float'), 
    "num_samps": uint32(297),
    "num_ranges": uint32(75),
    "pulses": array([0, 9, 12, 20, 22, 26, 27]).astype(uint32), 
    "lags": array([[ 0,  0],
                    [26, 27],
                    [20, 22],
                    [9, 12],
                    [22, 26],
                    [22, 27],
                    [20, 26],
                    [20, 27],
                    [12, 20],
                    [0, 9],
                    [12, 22],
                    [9, 20],
                    [0, 12],
                    [9, 22],
                    [12, 26],
                    [12, 27],
                    [9, 26],
                    [9, 27],
                    [0, 20],
                    [0, 22],
                    [0, 26],
                    [0, 27],
                    [27, 27]]).astype(uint32),
    "blanked_samples": array([0, 72, 96, 160, 176, 208, 216]).astype(uint32), 
    "sqn_timestamps": array([1.55858399e+09, 1.55858399e+09,
    1.55858399e+09, 1.55858399e+09, 1.55858399e+09, 1.55858399e+09, 
    1.55858399e+09, 1.55858399e+09, 1.55858399e+09, 1.55858399e+09, 
    1.55858399e+09, 1.55858399e+09, 1.55858399e+09, 1.55858399e+09, 
    1.55858399e+09, 1.55858399e+09, 1.55858399e+09, 1.55858399e+09, 
    1.55858399e+09, 1.55858399e+09, 1.55858399e+09, 1.55858399e+09, 
    1.55858399e+09, 1.55858399e+09, 1.55858399e+09, 1.55858399e+09, 
    1.55858399e+09, 1.55858399e+09, 1.55858399e+09]), 
    "beam_nums": array([0]).astype(uint32), 
    "beam_azms": array([0.0]), 
    "data_descriptors": array(['num_antenna_arrays', 'num_sequences', 
                                'num_beams', 'num_samps']), 
    "data_dimensions": array([2, 29, 1, 297]).astype(uint32), 
    "antenna_arrays_order": array(['main', 'intf']),
    "noise_at_freq": array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 
                             0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 
                             0., 0., 0., 0., 0., 0., 0.]), 
    "data_normalization_factor": float64(9999999.999999996),
    "data": zeros(17226).astype(complex64)
    })])

num_records = 1500
borealis_array_bfiq_data = {
    "borealis_git_hash": str_('v0.2-61-gc13ab34'), 
    "experiment_id": int64(100000000),
    "experiment_name": str_('TestScheme9ACFs'), 
    "experiment_comment": str_(''), 
    "num_slices": array([1] * num_records).astype(int64), 
    "slice_comment": str_(''), 
    "station": str_('sas'),
    "pulse_phase_offset": array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]).astype(float32),
    "range_sep": float32(44.96887), 
    "first_range_rtt": float32(1200.8307), 
    "first_range": float32(180.0), 
    "rx_sample_rate": float64(3333.3333333333335),
    "scan_start_marker": array([True] * num_records).astype(bool_), 
    "tx_pulse_len": uint32(300), 
    "tau_spacing": uint32(2400), 
    "main_antenna_count": uint32(16), 
    "intf_antenna_count": uint32(4), 
    "freq": uint32(10500), 
    "samples_data_type": str_('complex float'), 
    "num_samps": uint32(297),
    "num_ranges": uint32(75),
    "num_beams": array([1] * num_records).astype(uint32),
    "pulses": array([0, 9, 12, 20, 22, 26, 27]).astype(uint32), 
    "lags": array([[ 0,  0],
                    [26, 27],
                    [20, 22],
                    [9, 12],
                    [22, 26],
                    [22, 27],
                    [20, 26],
                    [20, 27],
                    [12, 20],
                    [0, 9],
                    [12, 22],
                    [9, 20],
                    [0, 12],
                    [9, 22],
                    [12, 26],
                    [12, 27],
                    [9, 26],
                    [9, 27],
                    [0, 20],
                    [0, 22],
                    [0, 26],
                    [0, 27],
                    [27, 27]]).astype(uint32),
    "blanked_samples": array([0, 72, 96, 160, 176, 208, 216]).astype(uint32), 
    "beam_nums": array([0] * num_records).astype(uint32), 
    "beam_azms": array([0.0] * num_records), 
    "data_descriptors": array(['num_records', 'num_antenna_arrays', 'num_sequences', 
                                'num_beams', 'num_samps']), 
    "data_normalization_factor": float64(9999999.999999996),
    "antenna_arrays_order": array(['main', 'intf']),
    "int_time": array([3.000395] * num_records).astype(float32), 
    "num_sequences": array([int64(29)] * num_records, dtype=int64), 
    "sqn_timestamps": array([[1.55858399e+09, 1.55858399e+09,
    1.55858399e+09, 1.55858399e+09, 1.55858399e+09, 1.55858399e+09, 
    1.55858399e+09, 1.55858399e+09, 1.55858399e+09, 1.55858399e+09, 
    1.55858399e+09, 1.55858399e+09, 1.55858399e+09, 1.55858399e+09, 
    1.55858399e+09, 1.55858399e+09, 1.55858399e+09, 1.55858399e+09, 
    1.55858399e+09, 1.55858399e+09, 1.55858399e+09, 1.55858399e+09, 
    1.55858399e+09, 1.55858399e+09, 1.55858399e+09, 1.55858399e+09, 
    1.55858399e+09, 1.55858399e+09, 1.55858399e+09]] * num_records), 
    "noise_at_freq": array([[0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 
                             0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 
                             0., 0., 0., 0., 0., 0., 0.]] * num_records), 
    "data": zeros((num_records, 17226)).astype(complex64)
    }
