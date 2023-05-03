# author: Jannes Spangenberg
# e-mail: jannes.spangenberg@uni-jena.de
# github: https://github.com/JannesSP
# website: https://jannessp.github.io

from read5.read5 import open
import numpy as np
import os

fast5_readidstarget = ['read_0005aa67-502b-4909-bc5e-e74e4a308151', 'read_0008609d-0d3e-46e5-9b69-25f7ab4b194e', 'read_000d4427-bc0c-42a5-a77d-3126c91ca17b', 'read_00118376-02d0-40a7-88db-5b450adebe13', 'read_0014e1e2-dc31-43d5-b055-564f2250e51f', 'read_00161499-b98a-4753-891d-1559cf020851', 'read_00277149-a710-4081-b5e5-726dffa961d4', 'read_003a1316-6363-4023-83e6-1f8acc32bad3', 'read_003deea8-84e6-4161-9659-12a9fee2cfd4', 'read_00425ffc-17d7-4ba0-87ae-9c01215661ca']
readidstarget = [read.split('read_')[-1] for read in fast5_readidstarget]
test_fast5 = os.path.join(os.path.dirname(__file__), 'test.fast5')
test_slow5 = os.path.join(os.path.dirname(__file__), 'test.slow5')
test_blow5 = os.path.join(os.path.dirname(__file__), 'test.blow5')
test_pod5 = os.path.join(os.path.dirname(__file__), 'test.pod5')

r = 0
signal_len_r = 23414
offset_r = -0.0
range_r = 1111.890380859375
digitisation_r = 8192.0
start_time_r = 443473
start_time_in_min_r = 2.453923196104471
channel_r = 143
sampling_rate_r = 3012
signal_r_first10 = [481, 477, 495, 495, 467, 479, 471, 485, 457, 463]
signal_r_last10 = [447, 558, 515, 471, 456, 481, 476, 629, 555, 578]
pASignal_r_first10 = [65.28555580973625, 64.74264058470726, 67.18575909733772, 67.18575909733772, 63.38535252213478, 65.01409819722176, 63.92826774716377, 65.82847103476524, 62.0280644595623, 62.84243729710579]
pASignal_r_last10 = [60.67077639698982, 75.73667389154434, 69.90033522248268, 63.92826774716377, 61.892335653305054, 65.28555580973625, 64.60691177845001, 85.37341913580894, 75.3294874727726, 78.4512500166893]
normSignal_r_first10 = [-0.5412580168639344, -0.5745662025170997, -0.42467936707785625, -0.42467936707785625, -0.6578366666500126, -0.5579121096905171, -0.6245284809968474, -0.5079498312107692, -0.7411071307829256, -0.6911448523031778]
normSignal_r_last10 = [-0.8243775949158386, 0.09992455695949559, -0.25813843881203025, -0.6245284809968474, -0.7494341771962169, -0.5412580168639344, -0.582893248930391, 0.6911448523031778, 0.0749434177196217, 0.26646548522532154]
# ============================================================================================
# Tests for fast5

def test_fast5_opens():
    f5 = open(test_fast5)
    assert f5.isOpen()
    f5.close()
    assert not f5.isOpen()

def test_fast5_ids():
    f5 = open(test_fast5)
    assert set(f5.getReads()) == set(fast5_readidstarget)
    f5.close()

def test_fast5_size():
    f5 = open(test_fast5)
    assert len(f5) == 10
    f5.close()

def test_fast5_getitem_with_iter():
    f5 = open(test_fast5)
    for readid in f5:
        assert 'Raw' in f5[readid].keys()
        assert 'channel_id' in f5[readid].keys()
        assert 'context_tags' in f5[readid].keys()
        assert 'tracking_id' in f5[readid].keys()
    f5.close()

def test_fast5_iter():
    f5 = open(test_fast5)
    for readid, target in zip(f5, fast5_readidstarget):
        assert readid == target
    f5.close()

def test_fast5_read_offset():
    f5 = open(test_fast5)
    assert f5.getOffset(fast5_readidstarget[0]) == offset_r
    f5.close()

def test_fast5_read_range():
    f5 = open(test_fast5)
    assert f5.getRange(fast5_readidstarget[0]) == range_r
    f5.close()

def test_fast5_read_digitisation():
    f5 = open(test_fast5)
    assert f5.getDigitisation(fast5_readidstarget[0]) == digitisation_r
    f5.close()

def test_pod5_read_calibration_scale():
    f5 = open(test_fast5)
    assert f5.getCalibrationScale(fast5_readidstarget[0]) == range_r / digitisation_r
    f5.close()

def test_fast5_read_signal():
    f5 = open(test_fast5)
    assert (f5.getSignal(fast5_readidstarget[0])[:10] == signal_r_first10).all()
    assert (f5.getSignal(fast5_readidstarget[0])[-10:] == signal_r_last10).all()
    assert len(f5.getSignal(fast5_readidstarget[0])) == signal_len_r
    f5.close()

def test_fast5_read_pASignal():
    f5 = open(test_fast5)
    assert (f5.getpASignal(fast5_readidstarget[0])[:10] == pASignal_r_first10).all()
    assert (f5.getpASignal(fast5_readidstarget[0])[-10:] == pASignal_r_last10).all()
    assert len(f5.getpASignal(fast5_readidstarget[0])) == signal_len_r
    f5.close()

def test_fast5_read_normSignal():
    f5 = open(test_fast5)
    assert (f5.getZNormSignal(fast5_readidstarget[0])[:10] == normSignal_r_first10).all()
    assert (f5.getZNormSignal(fast5_readidstarget[0])[-10:] == normSignal_r_last10).all()
    assert len(f5.getZNormSignal(fast5_readidstarget[0])) == signal_len_r
    f5.close()

def test_fast5_read_channel_number():
    f5 = open(test_fast5)
    assert f5.getChannel(fast5_readidstarget[0]) == channel_r
    f5.close()

def test_fast5_read_start_time():
    f5 = open(test_fast5)
    assert f5.getStartTime(fast5_readidstarget[0]) == start_time_r
    f5.close()

def test_fast5_read_start_time_in_minutes():
    f5 = open(test_fast5)
    assert f5.getStartTimeInMinutes(fast5_readidstarget[0]) == start_time_in_min_r
    f5.close()

def test_fast5_read_sampling_rate():
    f5 = open(test_fast5)
    assert f5.getSamplingRate(fast5_readidstarget[0]) == sampling_rate_r
    f5.close()

# ============================================================================================
# Tests for slow5

def test_slow5_opens():
    s5 = open(test_slow5)
    assert s5.isOpen()
    s5.close()
    assert not s5.isOpen()

def test_slow5_ids():
    s5 = open(test_slow5)
    assert set(s5.getReads()) == set(readidstarget)
    s5.close()

def test_slow5_getitem_with_iter():
    s5 = open(test_slow5)
    for readid in s5:
        assert 'read_id' in s5[readid]
        assert 'read_group' in s5[readid]
        assert 'digitisation' in s5[readid]
        assert 'offset' in s5[readid]
        assert 'range' in s5[readid]
        assert 'sampling_rate' in s5[readid]
        assert 'len_raw_signal' in s5[readid]
        assert 'signal' in s5[readid]
    s5.close()

def test_slow5_iter():
    s5 = open(test_slow5)
    for readid, target in zip(s5, readidstarget):
        assert readid == target
    s5.close()

def test_slow5_read_offset():
    s5 = open(test_slow5)
    assert s5.getOffset(readidstarget[0]) == offset_r
    s5.close()

def test_slow5_read_range():
    s5 = open(test_slow5)
    assert np.isclose(s5.getRange(readidstarget[0]), range_r)
    s5.close()

def test_slow5_read_digitisation():
    s5 = open(test_slow5)
    assert s5.getDigitisation(readidstarget[0]) == digitisation_r
    s5.close()

def test_pod5_read_calibration_scale():
    s5 = open(test_slow5)
    assert s5.getCalibrationScale(readidstarget[0]) == range_r / digitisation_r
    s5.close()

def test_slow5_read_signal():
    s5 = open(test_slow5)
    assert (s5.getSignal(readidstarget[0])[:10] == signal_r_first10).all()
    assert (s5.getSignal(readidstarget[0])[-10:] == signal_r_last10).all()
    assert len(s5.getSignal(readidstarget[0])) == signal_len_r
    s5.close()

def test_slow5_read_pASignal():
    s5 = open(test_slow5)
    assert np.isclose(s5.getpASignal(readidstarget[0])[:10], pASignal_r_first10).all()
    assert np.isclose(s5.getpASignal(readidstarget[0])[-10:], pASignal_r_last10).all()
    assert len(s5.getpASignal(readidstarget[0])) == signal_len_r
    s5.close()

def test_slow5_read_normSignal():
    s5 = open(test_slow5)
    assert np.isclose(s5.getZNormSignal(readidstarget[0])[:10], normSignal_r_first10).all()
    assert np.isclose(s5.getZNormSignal(readidstarget[0])[-10:], normSignal_r_last10).all()
    assert len(s5.getZNormSignal(readidstarget[0])) == signal_len_r
    s5.close()

def test_slow5_read_channel_number():
    s5 = open(test_slow5)
    assert s5.getChannel(readidstarget[0]) == channel_r
    s5.close()

def test_slow5_read_start_time():
    s5 = open(test_slow5)
    assert s5.getStartTime(readidstarget[0]) == start_time_r
    s5.close()

def test_slow5_read_sampling_rate():
    s5 = open(test_slow5)
    assert s5.getSamplingRate(readidstarget[0]) == sampling_rate_r
    s5.close()

def test_slow5_read_start_time_in_minutes():
    s5 = open(test_slow5)
    assert s5.getStartTimeInMinutes(readidstarget[0]) == start_time_in_min_r
    s5.close()

# ============================================================================================
# Tests for blow5

def test_blow5_opens():
    b5 = open(test_blow5)
    assert b5.isOpen()
    b5.close()
    assert not b5.isOpen()

def test_blow5_ids():
    b5 = open(test_blow5)
    assert set(b5.getReads()) == set(readidstarget)
    b5.close()

def test_blow5_getitem_with_iter():
    b5 = open(test_blow5)
    for readid in b5:
        assert 'read_id' in b5[readid]
        assert 'read_group' in b5[readid]
        assert 'digitisation' in b5[readid]
        assert 'offset' in b5[readid]
        assert 'range' in b5[readid]
        assert 'sampling_rate' in b5[readid]
        assert 'len_raw_signal' in b5[readid]
        assert 'signal' in b5[readid]
    b5.close()

def test_blow5_iter():
    b5 = open(test_slow5)
    for readid, target in zip(b5, readidstarget):
        assert readid == target
    b5.close()

def test_blow5_read_offset():
    b5 = open(test_blow5)
    assert b5.getOffset(readidstarget[0]) == offset_r
    b5.close()

def test_blow5_read_range():
    b5 = open(test_blow5)
    assert b5.getRange(readidstarget[0]) == range_r
    b5.close()

def test_blow5_read_digitisation():
    b5 = open(test_blow5)
    assert b5.getDigitisation(readidstarget[0]) == digitisation_r
    b5.close()

def test_pod5_read_calibration_scale():
    b5 = open(test_blow5)
    assert b5.getCalibrationScale(readidstarget[0]) == range_r / digitisation_r
    b5.close()

def test_blow5_read_signal():
    b5 = open(test_blow5)
    assert (b5.getSignal(readidstarget[0])[:10] == signal_r_first10).all()
    assert (b5.getSignal(readidstarget[0])[-10:] == signal_r_last10).all()
    assert len(b5.getSignal(readidstarget[0])) == signal_len_r
    b5.close()

def test_blow5_read_pASignal():
    b5 = open(test_blow5)
    assert np.isclose(b5.getpASignal(readidstarget[0])[:10], pASignal_r_first10).all()
    assert np.isclose(b5.getpASignal(readidstarget[0])[-10:], pASignal_r_last10).all()
    assert len(b5.getpASignal(readidstarget[0])) == signal_len_r
    b5.close()

def test_blow5_read_normSignal():
    b5 = open(test_blow5)
    assert np.isclose(b5.getZNormSignal(readidstarget[0])[:10], normSignal_r_first10).all()
    assert np.isclose(b5.getZNormSignal(readidstarget[0])[-10:], normSignal_r_last10).all()
    assert len(b5.getZNormSignal(readidstarget[0])) == signal_len_r
    b5.close()

def test_blow5_read_channel_number():
    b5 = open(test_blow5)
    assert b5.getChannel(readidstarget[0]) == channel_r
    b5.close()

def test_blow5_read_start_time():
    b5 = open(test_blow5)
    assert b5.getStartTime(readidstarget[0]) == start_time_r
    b5.close()

def test_blow5_read_start_time_in_minutes():
    b5 = open(test_blow5)
    assert b5.getStartTimeInMinutes(readidstarget[0]) == start_time_in_min_r
    b5.close()

def test_blow5_read_sampling_rate():
    b5 = open(test_blow5)
    assert b5.getSamplingRate(readidstarget[0]) == sampling_rate_r
    b5.close()

# ============================================================================================
# Tests for pod5

def test_pod5_opens():
    p5 = open(test_pod5)
    assert p5.isOpen()
    p5.close()
    assert not p5.isOpen()

def test_pod5_ids():
    p5 = open(test_pod5)
    assert set(p5.getReads()) == set(readidstarget)
    p5.close()

def test_pod5_getitem_with_iter():
    p5 = open(test_pod5)
    for readid in p5:
        assert p5[readid].read_id is not None
        assert p5[readid].calibration is not None
        assert p5[readid].end_reason is not None
        assert p5[readid].pore is not None
        assert p5[readid].read_number is not None
        assert p5[readid].run_info is not None
        assert p5[readid].signal is not None
    p5.close()

def test_pod5_iter():
    p5 = open(test_pod5)
    for readid, target in zip(p5, readidstarget):
        assert readid == target
    p5.close()

def test_pod5_read_offset():
    p5 = open(test_pod5)
    assert p5.getOffset(readidstarget[0]) == offset_r
    p5.close()

def test_pod5_read_calibration_scale():
    p5 = open(test_pod5)
    assert p5.getCalibrationScale(readidstarget[0]) == range_r / digitisation_r
    p5.close()

def test_pod5_read_signal():
    p5 = open(test_pod5)
    assert (p5.getSignal(readidstarget[0])[:10] == signal_r_first10).all()
    assert (p5.getSignal(readidstarget[0])[-10:] == signal_r_last10).all()
    assert len(p5.getSignal(readidstarget[0])) == signal_len_r
    p5.close()

def test_pod5_read_pASignal():
    p5 = open(test_pod5)
    assert np.isclose(p5.getpASignal(readidstarget[0])[:10], pASignal_r_first10).all()
    assert np.isclose(p5.getpASignal(readidstarget[0])[-10:], pASignal_r_last10).all()
    assert len(p5.getpASignal(readidstarget[0])) == signal_len_r
    p5.close()

def test_pod5_read_normSignal():
    p5 = open(test_pod5)
    assert np.isclose(p5.getZNormSignal(readidstarget[0])[:10], normSignal_r_first10).all()
    assert np.isclose(p5.getZNormSignal(readidstarget[0])[-10:], normSignal_r_last10).all()
    assert len(p5.getZNormSignal(readidstarget[0])) == signal_len_r
    p5.close()

def test_pod5_read_channel_number():
    p5 = open(test_pod5)
    assert p5.getChannel(readidstarget[0]) == channel_r
    p5.close()

def test_pod5_read_sampling_rate():
    p5 = open(test_pod5)
    assert p5.getSamplingRate(readidstarget[0]) == sampling_rate_r
    p5.close()
    
def test_fast5_read_start_time():
    p5 = open(test_pod5)
    assert p5.getStartTime(readidstarget[0]) == start_time_r
    p5.close()

def test_fast5_read_start_time_in_minutes():
    p5 = open(test_pod5)
    assert p5.getStartTimeInMinutes(readidstarget[0]) == start_time_in_min_r
    p5.close()