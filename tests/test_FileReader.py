# author: Jannes Spangenberg
# e-mail: jannes.spangenberg@uni-jena.de
# github: https://github.com/JannesSP
# website: https://jannessp.github.io

from read5.Reader import read
from read5.Exceptions import *
import numpy as np
import os

readidstarget = ['0005aa67-502b-4909-bc5e-e74e4a308151', '0008609d-0d3e-46e5-9b69-25f7ab4b194e', '000d4427-bc0c-42a5-a77d-3126c91ca17b', '00118376-02d0-40a7-88db-5b450adebe13', '0014e1e2-dc31-43d5-b055-564f2250e51f', '00161499-b98a-4753-891d-1559cf020851', '00277149-a710-4081-b5e5-726dffa961d4', '003a1316-6363-4023-83e6-1f8acc32bad3', '003deea8-84e6-4161-9659-12a9fee2cfd4', '00425ffc-17d7-4ba0-87ae-9c01215661ca']
# readidstarget = [read.split('read_')[-1] for read in readidstarget]
test_fast5 = os.path.join(os.path.dirname(__file__), 'test.fast5')
test_slow5 = os.path.join(os.path.dirname(__file__), 'test.slow5')
test_blow5 = os.path.join(os.path.dirname(__file__), 'test.blow5')
test_pod5 = os.path.join(os.path.dirname(__file__), 'test.pod5')

read_idx = 0

read_attrs_r = {'pore_type': b'not_set', 'run_id': b'65939f424626e8f63c24a2b2553bcea801dcd287'}

# read_raw_attrs_r = {'duration': 23414, 'end_reason': 5, 'median_before': 213.71470642089844, 'num_minknow_events': 562, 'num_reads_since_mux_change': 0, 'predicted_scaling_scale': np.nan, 'predicted_scaling_shift': np.nan, 'read_id': b'0005aa67-502b-4909-bc5e-e74e4a308151', 'read_number': 688, 'start_mux': 2, 'start_time': 443473, 'time_since_mux_change': 155.00896, 'tracked_scaling_scale': np.nan, 'tracked_scaling_shift': np.nan}
read_raw_attrs_r = {'duration': 23414, 'end_reason': 5, 'median_before': 213.71470642089844, 'num_minknow_events': 562, 'num_reads_since_mux_change': 0, 'read_id': b'0005aa67-502b-4909-bc5e-e74e4a308151', 'read_number': 688, 'start_mux': 2, 'start_time': 443473}

read_tracking_attrs_r = {'asic_id': b'751497074', 'asic_id_eeprom': b'8103331', 'asic_temp': b'24.137976', 'asic_version': b'IA02D', 'auto_update': b'0', 'auto_update_source': b'https://cdn.oxfordnanoportal.com/software/MinKNOW/', 'bream_is_standard': b'0', 'configuration_version': b'5.4.7', 'device_id': b'MN21435', 'device_type': b'minion', 'distribution_status': b'stable', 'distribution_version': b'22.12.7', 'exp_script_name': b'sequencing/sequencing_MIN106_RNA:FLO-MIN106:SQK-RNA002', 'exp_script_purpose': b'sequencing_run', 'exp_start_time': b'2023-03-16T15:24:42.710504+01:00', 'flow_cell_id': b'FAU48364', 'flow_cell_product_code': b'FLO-MIN106', 'guppy_version': b'6.4.6+ae70e8f', 'heatsink_temp': b'33.921875', 'host_product_code': b'unknown', 'host_product_serial_number': b'', 'hostname': b'Acer-bioinf3', 'installation_type': b'nc', 'local_firmware_file': b'1', 'operating_system': b'ubuntu 20.04', 'protocol_group_id': b'Rmo_20230316_ID5s10_r1_FAU48364_LG', 'protocol_run_id': b'f1cc8db3-5599-43c4-8341-3b33d8fa024d', 'protocol_start_time': b'2023-03-16T15:19:23.820855+01:00', 'protocols_version': b'7.4.8', 'run_id': b'65939f424626e8f63c24a2b2553bcea801dcd287', 'sample_id': b'Rmo_20230316_ID5s10_r1_FAU48364_LG', 'usb_config': b'fx3_1.2.5#fpga_1.2.1#bulk#USB300', 'version': b'5.4.3'}

read_channel_attrs_r = {'channel_number': b'143', 'digitisation': 8192.0, 'offset': -0.0, 'range': 1111.890380859375, 'sampling_rate': 3012.0}

read_context_attrs_r = {'barcoding_enabled': b'0', 'experiment_duration_set': b'4320', 'experiment_type': b'rna', 'local_basecalling': b'0', 'package': b'bream4', 'package_version': b'7.4.8', 'sample_frequency': b'3012', 'sequencing_kit': b'sqk-rna002'}

start_time_in_min_r = 2.453923196104471
signal_r_first10 = [481, 477, 495, 495, 467, 479, 471, 485, 457, 463]
signal_r_last10 = [447, 558, 515, 471, 456, 481, 476, 629, 555, 578]
pASignal_r_first10 = [65.28555580973625, 64.74264058470726, 67.18575909733772, 67.18575909733772, 63.38535252213478, 65.01409819722176, 63.92826774716377, 65.82847103476524, 62.0280644595623, 62.84243729710579]
pASignal_r_last10 = [60.67077639698982, 75.73667389154434, 69.90033522248268, 63.92826774716377, 61.892335653305054, 65.28555580973625, 64.60691177845001, 85.37341913580894, 75.3294874727726, 78.4512500166893]
normSignal_r_first10 = [-0.5412580168639344, -0.5745662025170997, -0.42467936707785625, -0.42467936707785625, -0.6578366666500126, -0.5579121096905171, -0.6245284809968474, -0.5079498312107692, -0.7411071307829256, -0.6911448523031778]
normSignal_r_last10 = [-0.8243775949158386, 0.09992455695949559, -0.25813843881203025, -0.6245284809968474, -0.7494341771962169, -0.5412580168639344, -0.582893248930391, 0.6911448523031778, 0.0749434177196217, 0.26646548522532154]

# ============================================================================================
def test_file_format_exception():
    try:
        read('test')
    except Exception as e:
        assert isinstance(e, UnknownFileFormatException)

def test_normalization_exception():
    f5 = read(test_fast5)
    try:
        f5.getZNormSignal(readidstarget[read_idx], 'maximum')
    except Exception as e:
        assert isinstance(e, UnknownNormalizationMode)

# Tests for fast5
fast5_file_version = '2.0'

def test_fast5_opens():
    f5 = read(test_fast5)
    assert f5.isOpen()
    f5.close()
    assert not f5.isOpen()

def test_fast5_ids():
    f5 = read(test_fast5)
    assert set(f5.getReads()) == set(readidstarget)
    f5.close()

def test_fast5_size():
    f5 = read(test_fast5)
    assert len(f5) == 10
    f5.close()

def test_fast5_getitem_with_iter():
    f5 = read(test_fast5)
    for readid in f5:
        assert 'Raw' in f5[readid].keys()
        assert 'channel_id' in f5[readid].keys()
        assert 'context_tags' in f5[readid].keys()
        assert 'tracking_id' in f5[readid].keys()
    f5.close()

def test_fast5_iter():
    f5 = read(test_fast5)
    for readid, target in zip(f5, readidstarget):
        assert readid == target
    f5.close()

def test_fast5_offset():
    f5 = read(test_fast5)
    assert f5.getOffset(readidstarget[read_idx]) == read_channel_attrs_r['offset']
    f5.close()

def test_fast5_range():
    f5 = read(test_fast5)
    assert f5.getRange(readidstarget[read_idx]) == read_channel_attrs_r['range']
    f5.close()

def test_fast5_digitisation():
    f5 = read(test_fast5)
    assert f5.getDigitisation(readidstarget[read_idx]) == read_channel_attrs_r['digitisation']
    f5.close()

def test_fast5_calibration_scale():
    f5 = read(test_fast5)
    assert f5.getCalibrationScale(readidstarget[read_idx]) == read_channel_attrs_r['range'] / read_channel_attrs_r['digitisation']
    f5.close()

def test_fast5_signal():
    f5 = read(test_fast5)
    assert (f5.getSignal(readidstarget[read_idx])[:10] == signal_r_first10).all()
    assert (f5.getSignal(readidstarget[read_idx])[-10:] == signal_r_last10).all()
    assert len(f5.getSignal(readidstarget[read_idx])) == read_raw_attrs_r['duration']
    f5.close()

def test_fast5_pASignal():
    f5 = read(test_fast5)
    assert (f5.getpASignal(readidstarget[read_idx])[:10] == pASignal_r_first10).all()
    assert (f5.getpASignal(readidstarget[read_idx])[-10:] == pASignal_r_last10).all()
    assert len(f5.getpASignal(readidstarget[read_idx])) == read_raw_attrs_r['duration']
    f5.close()

def test_fast5_normSignal():
    f5 = read(test_fast5)
    assert (f5.getZNormSignal(readidstarget[read_idx])[:10] == normSignal_r_first10).all()
    assert (f5.getZNormSignal(readidstarget[read_idx])[-10:] == normSignal_r_last10).all()
    assert len(f5.getZNormSignal(readidstarget[read_idx])) == read_raw_attrs_r['duration']
    f5.close()

def test_fast5_channel_number():
    f5 = read(test_fast5)
    assert f5.getChannelNumber(readidstarget[read_idx]) == int(read_channel_attrs_r['channel_number'])
    f5.close()

def test_fast5_start_time():
    f5 = read(test_fast5)
    assert f5.getStartTime(readidstarget[read_idx]) == read_raw_attrs_r['start_time']
    f5.close()

def test_fast5_sampling_rate():
    f5 = read(test_fast5)
    assert f5.getSamplingRate(readidstarget[read_idx]) == read_channel_attrs_r['sampling_rate']
    f5.close()

def test_fast5_start_time_in_minutes():
    f5 = read(test_fast5)
    assert f5.getStartTimeInMinutes(readidstarget[read_idx]) == start_time_in_min_r
    f5.close()

def test_fast5_file_version():
    f5 = read(test_fast5)
    assert f5.getFileVersion() == fast5_file_version
    f5.close()

def test_fast5_attributes():
    f5 = read(test_fast5)
    assert f5.getGlobalReadAttributes(readidstarget[read_idx]) == read_attrs_r
    f5.close()

def test_fast5_pore_type():
    f5 = read(test_fast5)
    assert f5.getPoreType(readidstarget[read_idx]) == read_attrs_r['pore_type'].decode('utf-8')
    f5.close()

def test_fast5_run_id():
    f5 = read(test_fast5)
    assert f5.getRunID(readidstarget[read_idx]) == read_tracking_attrs_r['run_id'].decode('utf-8')
    f5.close()

def test_fast5_raw_attributes():
    f5 = read(test_fast5)
    d = f5.getRawAttributs(readidstarget[read_idx])
    assert np.isnan(d['predicted_scaling_scale'])
    del d['predicted_scaling_scale']
    assert np.isnan(d['predicted_scaling_shift'])
    del d['predicted_scaling_shift']
    assert np.isnan(d['tracked_scaling_scale'])
    del d['tracked_scaling_scale']
    assert np.isnan(d['tracked_scaling_shift'])
    del d['tracked_scaling_shift']
    assert np.isclose(d['time_since_mux_change'], 155.00896)
    del d['time_since_mux_change']
    assert d == read_raw_attrs_r
    f5.close()

def test_fast5_duration():
    f5 = read(test_fast5)
    assert f5.getDuration(readidstarget[read_idx]) == read_raw_attrs_r['duration']
    f5.close()

def test_fast5_end_reason():
    f5 = read(test_fast5)
    assert f5.getEndReason(readidstarget[read_idx]) == read_raw_attrs_r['end_reason']
    f5.close()

def test_fast5_median_before():
    f5 = read(test_fast5)
    assert f5.getMedianBefore(readidstarget[read_idx]) == read_raw_attrs_r['median_before']
    f5.close()

def test_fast5_minknow_events():
    f5 = read(test_fast5)
    assert f5.getNumMinknowEvents(readidstarget[read_idx]) == read_raw_attrs_r['num_minknow_events']
    f5.close()

def test_fast5_reads_since_mux_change():
    f5 = read(test_fast5)
    assert f5.getNumReadsSinceMuxChange(readidstarget[read_idx]) == read_raw_attrs_r['num_reads_since_mux_change']
    f5.close()

def test_fast5_predicted_scaling():
    f5 = read(test_fast5)
    assert np.isnan(f5.getPredictedScaling(readidstarget[read_idx])).all()
    f5.close()

def test_fast5_number():
    f5 = read(test_fast5)
    assert f5.getReadNumber(readidstarget[read_idx]) == read_raw_attrs_r['read_number']
    f5.close()

def test_fast5_start_mux():
    f5 = read(test_fast5)
    assert f5.getStartMux(readidstarget[read_idx]) == read_raw_attrs_r['start_mux']
    f5.close()

def test_fast5_start_time():
    f5 = read(test_fast5)
    assert f5.getStartTime(readidstarget[read_idx]) == read_raw_attrs_r['start_time']
    f5.close()

def test_fast5_time_since_mux_change():
    f5 = read(test_fast5)
    assert np.isclose(f5.getTimeSinceMuxChange(readidstarget[read_idx]), 155.00896)
    f5.close()

def test_fast5_tracked_scaling_scale():
    f5 = read(test_fast5)
    assert np.isnan(f5.getTrackedScalingScale(readidstarget[read_idx]))
    f5.close()

def test_fast5_tracked_scaling_shift():
    f5 = read(test_fast5)
    assert np.isnan(f5.getTrackedScalingShift(readidstarget[read_idx]))
    f5.close()

def test_fast5_channel_id_attributes():
    f5 = read(test_fast5)
    assert f5.getChannelIDAttributes(readidstarget[read_idx]) == read_channel_attrs_r
    f5.close()

def test_fast5_channel_number():
    f5 = read(test_fast5)
    assert f5.getChannelNumber(readidstarget[read_idx]) == int(read_channel_attrs_r['channel_number'])
    f5.close()

def test_fast5_context_tags_attributes():
    f5 = read(test_fast5)
    assert f5.getContextTagsAttributes(readidstarget[read_idx]) == read_context_attrs_r
    f5.close()

def test_fast5_barcoding_enabled():
    f5 = read(test_fast5)
    assert f5.isBarcodingEnabled(readidstarget[read_idx]) == bool(int(read_context_attrs_r['barcoding_enabled']))
    f5.close()

def test_fast5_experiment_duration():
    f5 = read(test_fast5)
    assert f5.getExperimentDurationSet(readidstarget[read_idx]) == int(read_context_attrs_r['experiment_duration_set'])
    f5.close()

def test_fast5_experiment_type():
    f5 = read(test_fast5)
    assert f5.getExperimentType(readidstarget[read_idx]) == read_context_attrs_r['experiment_type'].decode('utf-8')
    f5.close()

def test_fast5_local_basecalled():
    f5 = read(test_fast5)
    assert f5.isLocalBasecalled(readidstarget[read_idx]) == bool(int(read_context_attrs_r['local_basecalling']))
    f5.close()

def test_fast5_package():
    f5 = read(test_fast5)
    assert f5.getPackage(readidstarget[read_idx]) == read_context_attrs_r['package'].decode('utf-8')
    f5.close()

def test_fast5_package_version():
    f5 = read(test_fast5)
    assert f5.getPackageVersion(readidstarget[read_idx]) == read_context_attrs_r['package_version'].decode('utf-8')
    f5.close()

def test_fast5_sequencing_kit():
    f5 = read(test_fast5)
    assert f5.getSequencingKit(readidstarget[read_idx]) == read_context_attrs_r['sequencing_kit'].decode('utf-8')
    f5.close()

def test_fast5_tracking_attributes():
    f5 = read(test_fast5)
    assert f5.getTrackingIDAttributes(readidstarget[read_idx]) == read_tracking_attrs_r
    f5.close()

def test_fast5_asic_id():
    f5 = read(test_fast5)
    assert f5.getAsicID(readidstarget[read_idx]) == read_tracking_attrs_r['asic_id'].decode('utf-8')
    f5.close()

def test_fast5_asic_eeprom():
    f5 = read(test_fast5)
    assert f5.getAsicIDEeprom(readidstarget[read_idx]) == read_tracking_attrs_r['asic_id_eeprom'].decode('utf-8')
    f5.close()

def test_fast5_asic_temp():
    f5 = read(test_fast5)
    assert f5.getAsicTemp(readidstarget[read_idx]) == float(read_tracking_attrs_r['asic_temp'])
    f5.close()

def test_fast5_asic_version():
    f5 = read(test_fast5)
    assert f5.getAsicVersion(readidstarget[read_idx]) == read_tracking_attrs_r['asic_version'].decode('utf-8')
    f5.close()

def test_fast5_auto_update():
    f5 = read(test_fast5)
    assert f5.isAutoUpdated(readidstarget[read_idx]) == bool(int(read_tracking_attrs_r['auto_update']))
    f5.close()

def test_fast5_auto_update_source():
    f5 = read(test_fast5)
    assert f5.getAutoUpdateSource(readidstarget[read_idx]) == read_tracking_attrs_r['auto_update_source'].decode('utf-8')
    f5.close()

def test_fast5_bream_standard():
    f5 = read(test_fast5)
    assert f5.isBreamStandard(readidstarget[read_idx]) == bool(int(read_tracking_attrs_r['bream_is_standard']))
    f5.close()

def test_fast5_config_version():
    f5 = read(test_fast5)
    assert f5.getConfigurationVersion(readidstarget[read_idx]) == read_tracking_attrs_r['configuration_version'].decode('utf-8')
    f5.close()

def test_fast5_device_id():
    f5 = read(test_fast5)
    assert f5.getDeviceID(readidstarget[read_idx]) == read_tracking_attrs_r['device_id'].decode('utf-8')
    f5.close()

def test_fast5_device_type():
    f5 = read(test_fast5)
    assert f5.getDeviceType(readidstarget[read_idx]) == read_tracking_attrs_r['device_type'].decode('utf-8')
    f5.close()

def test_fast5_distribution_status():
    f5 = read(test_fast5)
    assert f5.getDistributionStatus(readidstarget[read_idx]) == read_tracking_attrs_r['distribution_status'].decode('utf-8')
    f5.close()

def test_fast5_distribution_version():
    f5 = read(test_fast5)
    assert f5.getDistributionVersion(readidstarget[read_idx]) == read_tracking_attrs_r['distribution_version'].decode('utf-8')
    f5.close()

def test_fast5_exp_script_name():
    f5 = read(test_fast5)
    assert f5.getExpScriptPurpose(readidstarget[read_idx]) == read_tracking_attrs_r['exp_script_purpose'].decode('utf-8')
    f5.close()

def test_fast5_exp_time_start():
    f5 = read(test_fast5)
    assert f5.getExpStartTime(readidstarget[read_idx]) == read_tracking_attrs_r['exp_start_time'].decode('utf-8')
    f5.close()

def test_fast5_flow_cell():
    f5 = read(test_fast5)
    assert f5.getFlowCellID(readidstarget[read_idx]) == read_tracking_attrs_r['flow_cell_id'].decode('utf-8')
    f5.close()

def test_fast5_flow_cell_product():
    f5 = read(test_fast5)
    assert f5.getFlowCellProductCode(readidstarget[read_idx]) == read_tracking_attrs_r['flow_cell_product_code'].decode('utf-8')
    f5.close()

def test_fast5_guppy_version():
    f5 = read(test_fast5)
    assert f5.getGuppyVersion(readidstarget[read_idx]) == read_tracking_attrs_r['guppy_version'].decode('utf-8')
    f5.close()

def test_fast5_heat_sink():
    f5 = read(test_fast5)
    assert f5.getHeatSinkTemp(readidstarget[read_idx]) == float(read_tracking_attrs_r['heatsink_temp'])
    f5.close()

def test_fast5_host_product_code():
    f5 = read(test_fast5)
    assert f5.getHostProductCode(readidstarget[read_idx]) == read_tracking_attrs_r['host_product_code'].decode('utf-8')
    f5.close()

def test_fast5_host_product_number():
    f5 = read(test_fast5)
    assert f5.getHostProductSerialNumber(readidstarget[read_idx]) == read_tracking_attrs_r['host_product_serial_number'].decode('utf-8')
    f5.close()

def test_fast5_hostname():
    f5 = read(test_fast5)
    assert f5.getHostname(readidstarget[read_idx]) == read_tracking_attrs_r['hostname'].decode('utf-8')
    f5.close()

def test_fast5_installation_type():
    f5 = read(test_fast5)
    assert f5.getInstallationType(readidstarget[read_idx]) == read_tracking_attrs_r['installation_type'].decode('utf-8')
    f5.close()

def test_fast5_local_firmware_file():
    f5 = read(test_fast5)
    assert f5.getLocalFirmwareFile(readidstarget[read_idx]) == int(read_tracking_attrs_r['local_firmware_file'])
    f5.close()

def test_fast5_os():
    f5 = read(test_fast5)
    assert f5.getOperatingSystem(readidstarget[read_idx]) == read_tracking_attrs_r['operating_system'].decode('utf-8')
    f5.close()

def test_fast5_prot_goup_id():
    f5 = read(test_fast5)
    assert f5.getProtocolGroupID(readidstarget[read_idx]) == read_tracking_attrs_r['protocol_group_id'].decode('utf-8')
    f5.close()

def test_fast5_prot_run_id():
    f5 = read(test_fast5)
    assert f5.getProtocolRunID(readidstarget[read_idx]) == read_tracking_attrs_r['protocol_run_id'].decode('utf-8')
    f5.close()

def test_fast5_prot_start_time():
    f5 = read(test_fast5)
    assert f5.getProtocolStartTime(readidstarget[read_idx]) == read_tracking_attrs_r['protocol_start_time'].decode('utf-8')
    f5.close()

def test_fast5_prot_version():
    f5 = read(test_fast5)
    assert f5.getProtocolVersion(readidstarget[read_idx]) == read_tracking_attrs_r['protocols_version'].decode('utf-8')
    f5.close()

def test_fast5_run_id():
    f5 = read(test_fast5)
    assert f5.getRunID(readidstarget[read_idx]) == read_tracking_attrs_r['run_id'].decode('utf-8')
    f5.close()

def test_fast5_sample_id():
    f5 = read(test_fast5)
    assert f5.getSampleID(readidstarget[read_idx]) == read_tracking_attrs_r['sample_id'].decode('utf-8')
    f5.close()

def test_fast5_usb():
    f5 = read(test_fast5)
    assert f5.getUSBConfig(readidstarget[read_idx]) == read_tracking_attrs_r['usb_config'].decode('utf-8')
    f5.close()

def test_fast5_version():
    f5 = read(test_fast5)
    assert f5.getVersion(readidstarget[read_idx]) == read_tracking_attrs_r['version'].decode('utf-8')
    f5.close()

# ============================================================================================
# Tests for slow5

slow5_blow5_file_version = '3.2'

def test_slow5_opens():
    s5 = read(test_slow5)
    assert s5.isOpen()
    s5.close()
    assert not s5.isOpen()

def test_slow5_ids():
    s5 = read(test_slow5)
    assert set(s5.getReads()) == set(readidstarget)
    s5.close()

def test_slow5_getitem_with_iter():
    s5 = read(test_slow5)
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
    s5 = read(test_slow5)
    for readid, target in zip(s5, readidstarget):
        assert readid == target
    s5.close()

def test_slow5_offset():
    s5 = read(test_slow5)
    assert s5.getOffset(readidstarget[read_idx]) == read_channel_attrs_r['offset']
    s5.close()

def test_slow5_range():
    s5 = read(test_slow5)
    assert np.isclose(s5.getRange(readidstarget[read_idx]), read_channel_attrs_r['range'])
    s5.close()

def test_slow5_digitisation():
    s5 = read(test_slow5)
    assert s5.getDigitisation(readidstarget[read_idx]) == read_channel_attrs_r['digitisation']
    s5.close()

def test_slow5_calibration_scale():
    s5 = read(test_slow5)
    assert np.isclose(s5.getCalibrationScale(readidstarget[read_idx]), read_channel_attrs_r['range'] / read_channel_attrs_r['digitisation'])
    s5.close()

def test_slow5_signal():
    s5 = read(test_slow5)
    assert (s5.getSignal(readidstarget[read_idx])[:10] == signal_r_first10).all()
    assert (s5.getSignal(readidstarget[read_idx])[-10:] == signal_r_last10).all()
    assert len(s5.getSignal(readidstarget[read_idx])) == read_raw_attrs_r['duration']
    s5.close()

def test_slow5_pASignal():
    s5 = read(test_slow5)
    assert np.isclose(s5.getpASignal(readidstarget[read_idx])[:10], pASignal_r_first10).all()
    assert np.isclose(s5.getpASignal(readidstarget[read_idx])[-10:], pASignal_r_last10).all()
    assert len(s5.getpASignal(readidstarget[read_idx])) == read_raw_attrs_r['duration']
    s5.close()

def test_slow5_normSignal():
    s5 = read(test_slow5)
    assert np.isclose(s5.getZNormSignal(readidstarget[read_idx])[:10], normSignal_r_first10).all()
    assert np.isclose(s5.getZNormSignal(readidstarget[read_idx])[-10:], normSignal_r_last10).all()
    assert len(s5.getZNormSignal(readidstarget[read_idx])) == read_raw_attrs_r['duration']
    s5.close()

def test_slow5_channel_number():
    s5 = read(test_slow5)
    assert s5.getChannelNumber(readidstarget[read_idx]) == int(read_channel_attrs_r['channel_number'])
    s5.close()

def test_slow5_start_time():
    s5 = read(test_slow5)
    assert s5.getStartTime(readidstarget[read_idx]) == read_raw_attrs_r['start_time']
    s5.close()

def test_slow5_sampling_rate():
    s5 = read(test_slow5)
    assert s5.getSamplingRate(readidstarget[read_idx]) == read_channel_attrs_r['sampling_rate']
    s5.close()

def test_slow5_start_time_in_minutes():
    s5 = read(test_slow5)
    assert s5.getStartTimeInMinutes(readidstarget[read_idx]) == start_time_in_min_r
    s5.close()

def test_slow5_file_version():
    s5 = read(test_slow5)
    assert s5.getFileVersion() == slow5_blow5_file_version
    s5.close()

def test_slow5_pore_type():
    s5 = read(test_slow5)
    assert s5.getPoreType() == read_attrs_r['pore_type'].decode('utf-8')
    s5.close()

def test_slow5_run_id():
    s5 = read(test_slow5)
    assert s5.getRunID() == read_tracking_attrs_r['run_id'].decode('utf-8')
    s5.close()

def test_slow5_duration():
    s5 = read(test_slow5)
    assert s5.getDuration(readidstarget[read_idx]) == read_raw_attrs_r['duration']
    s5.close()

def test_slow5_end_reason():
    s5 = read(test_slow5)
    assert s5.getEndReason(readidstarget[read_idx]) == read_raw_attrs_r['end_reason']
    s5.close()

def test_slow5_median_before():
    s5 = read(test_slow5)
    assert np.isclose(s5.getMedianBefore(readidstarget[read_idx]), read_raw_attrs_r['median_before'])
    s5.close()

def test_slow5_number():
    s5 = read(test_slow5)
    assert s5.getReadNumber(readidstarget[read_idx]) == read_raw_attrs_r['read_number']
    s5.close()

def test_slow5_start_mux():
    s5 = read(test_slow5)
    assert s5.getStartMux(readidstarget[read_idx]) == read_raw_attrs_r['start_mux']
    s5.close()

def test_slow5_start_time():
    s5 = read(test_slow5)
    assert s5.getStartTime(readidstarget[read_idx]) == read_raw_attrs_r['start_time']
    s5.close()

def test_slow5_channel_number():
    s5 = read(test_slow5)
    assert s5.getChannelNumber(readidstarget[read_idx]) == int(read_channel_attrs_r['channel_number'])
    s5.close()

def test_slow5_barcoding_enabled():
    s5 = read(test_slow5)
    assert s5.isBarcodingEnabled() == bool(int(read_context_attrs_r['barcoding_enabled']))
    s5.close()

def test_slow5_experiment_duration():
    s5 = read(test_slow5)
    assert s5.getExperimentDurationSet() == int(read_context_attrs_r['experiment_duration_set'])
    s5.close()

def test_slow5_experiment_type():
    s5 = read(test_slow5)
    assert s5.getExperimentType() == read_context_attrs_r['experiment_type'].decode('utf-8')
    s5.close()

def test_slow5_local_basecalled():
    s5 = read(test_slow5)
    assert s5.isLocalBasecalled() == bool(int(read_context_attrs_r['local_basecalling']))
    s5.close()

def test_slow5_package():
    s5 = read(test_slow5)
    assert s5.getPackage() == read_context_attrs_r['package'].decode('utf-8')
    s5.close()

def test_slow5_package_version():
    s5 = read(test_slow5)
    assert s5.getPackageVersion() == read_context_attrs_r['package_version'].decode('utf-8')
    s5.close()

def test_slow5_sequencing_kit():
    s5 = read(test_slow5)
    assert s5.getSequencingKit() == read_context_attrs_r['sequencing_kit'].decode('utf-8')
    s5.close()

def test_slow5_asic_id():
    s5 = read(test_slow5)
    assert s5.getAsicID() == read_tracking_attrs_r['asic_id'].decode('utf-8')
    s5.close()

def test_slow5_asic_eeprom():
    s5 = read(test_slow5)
    assert s5.getAsicIDEeprom() == read_tracking_attrs_r['asic_id_eeprom'].decode('utf-8')
    s5.close()

def test_slow5_asic_temp():
    s5 = read(test_slow5)
    assert s5.getAsicTemp() == float(read_tracking_attrs_r['asic_temp'])
    s5.close()

def test_slow5_asic_version():
    s5 = read(test_slow5)
    assert s5.getAsicVersion() == read_tracking_attrs_r['asic_version'].decode('utf-8')
    s5.close()

def test_slow5_auto_update():
    s5 = read(test_slow5)
    assert s5.isAutoUpdated() == bool(int(read_tracking_attrs_r['auto_update']))
    s5.close()

def test_slow5_auto_update_source():
    s5 = read(test_slow5)
    assert s5.getAutoUpdateSource() == read_tracking_attrs_r['auto_update_source'].decode('utf-8')
    s5.close()

def test_slow5_bream_standard():
    s5 = read(test_slow5)
    assert s5.isBreamStandard() == bool(int(read_tracking_attrs_r['bream_is_standard']))
    s5.close()

def test_slow5_config_version():
    s5 = read(test_slow5)
    assert s5.getConfigurationVersion() == read_tracking_attrs_r['configuration_version'].decode('utf-8')
    s5.close()

def test_slow5_device_id():
    s5 = read(test_slow5)
    assert s5.getDeviceID() == read_tracking_attrs_r['device_id'].decode('utf-8')
    s5.close()

def test_slow5_device_type():
    s5 = read(test_slow5)
    assert s5.getDeviceType() == read_tracking_attrs_r['device_type'].decode('utf-8')
    s5.close()

def test_slow5_distribution_status():
    s5 = read(test_slow5)
    assert s5.getDistributionStatus() == read_tracking_attrs_r['distribution_status'].decode('utf-8')
    s5.close()

def test_slow5_distribution_version():
    s5 = read(test_slow5)
    assert s5.getDistributionVersion() == read_tracking_attrs_r['distribution_version'].decode('utf-8')
    s5.close()

def test_slow5_exp_script_name():
    s5 = read(test_slow5)
    assert s5.getExpScriptPurpose() == read_tracking_attrs_r['exp_script_purpose'].decode('utf-8')
    s5.close()

def test_slow5_exp_time_start():
    s5 = read(test_slow5)
    assert s5.getExpStartTime() == read_tracking_attrs_r['exp_start_time'].decode('utf-8')
    s5.close()

def test_slow5_flow_cell():
    s5 = read(test_slow5)
    assert s5.getFlowCellID() == read_tracking_attrs_r['flow_cell_id'].decode('utf-8')
    s5.close()

def test_slow5_flow_cell_product():
    s5 = read(test_slow5)
    assert s5.getFlowCellProductCode() == read_tracking_attrs_r['flow_cell_product_code'].decode('utf-8')
    s5.close()

def test_slow5_guppy_version():
    s5 = read(test_slow5)
    assert s5.getGuppyVersion() == read_tracking_attrs_r['guppy_version'].decode('utf-8')
    s5.close()

def test_slow5_heat_sink():
    s5 = read(test_slow5)
    assert s5.getHeatSinkTemp() == float(read_tracking_attrs_r['heatsink_temp'])
    s5.close()

def test_slow5_host_product_code():
    s5 = read(test_slow5)
    assert s5.getHostProductCode() == read_tracking_attrs_r['host_product_code'].decode('utf-8')
    s5.close()

def test_slow5_host_product_number():
    s5 = read(test_slow5)
    assert s5.getHostProductSerialNumber() == read_tracking_attrs_r['host_product_serial_number'].decode('utf-8')
    s5.close()

def test_slow5_hostname():
    s5 = read(test_slow5)
    assert s5.getHostname() == read_tracking_attrs_r['hostname'].decode('utf-8')
    s5.close()

def test_slow5_installation_type():
    s5 = read(test_slow5)
    assert s5.getInstallationType() == read_tracking_attrs_r['installation_type'].decode('utf-8')
    s5.close()

def test_slow5_local_firmware_file():
    s5 = read(test_slow5)
    assert s5.getLocalFirmwareFile() == int(read_tracking_attrs_r['local_firmware_file'])
    s5.close()

def test_slow5_os():
    s5 = read(test_slow5)
    assert s5.getOperatingSystem() == read_tracking_attrs_r['operating_system'].decode('utf-8')
    s5.close()

def test_slow5_prot_goup_id():
    s5 = read(test_slow5)
    assert s5.getProtocolGroupID() == read_tracking_attrs_r['protocol_group_id'].decode('utf-8')
    s5.close()

def test_slow5_prot_run_id():
    s5 = read(test_slow5)
    assert s5.getProtocolRunID() == read_tracking_attrs_r['protocol_run_id'].decode('utf-8')
    s5.close()

def test_slow5_prot_start_time():
    s5 = read(test_slow5)
    assert s5.getProtocolStartTime() == read_tracking_attrs_r['protocol_start_time'].decode('utf-8')
    s5.close()

def test_slow5_prot_version():
    s5 = read(test_slow5)
    assert s5.getProtocolVersion() == read_tracking_attrs_r['protocols_version'].decode('utf-8')
    s5.close()

def test_slow5_run_id():
    s5 = read(test_slow5)
    assert s5.getRunID() == read_tracking_attrs_r['run_id'].decode('utf-8')
    s5.close()

def test_slow5_sample_id():
    s5 = read(test_slow5)
    assert s5.getSampleID() == read_tracking_attrs_r['sample_id'].decode('utf-8')
    s5.close()

def test_slow5_usb():
    s5 = read(test_slow5)
    assert s5.getUSBConfig() == read_tracking_attrs_r['usb_config'].decode('utf-8')
    s5.close()

def test_slow5_version():
    s5 = read(test_slow5)
    assert s5.getVersion() == read_tracking_attrs_r['version'].decode('utf-8')
    s5.close()

# ============================================================================================
# Tests for blow5

def test_blow5_opens():
    b5 = read(test_blow5)
    assert b5.isOpen()
    b5.close()
    assert not b5.isOpen()

def test_blow5_ids():
    b5 = read(test_blow5)
    assert set(b5.getReads()) == set(readidstarget)
    b5.close()

def test_blow5_getitem_with_iter():
    b5 = read(test_blow5)
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
    b5 = read(test_slow5)
    for readid, target in zip(b5, readidstarget):
        assert readid == target
    b5.close()

def test_blow5_offset():
    b5 = read(test_blow5)
    assert b5.getOffset(readidstarget[read_idx]) == read_channel_attrs_r['offset']
    b5.close()

def test_blow5_range():
    b5 = read(test_blow5)
    assert b5.getRange(readidstarget[read_idx]) == read_channel_attrs_r['range']
    b5.close()

def test_blow5_digitisation():
    b5 = read(test_blow5)
    assert b5.getDigitisation(readidstarget[read_idx]) == read_channel_attrs_r['digitisation']
    b5.close()

def test_blow5_calibration_scale():
    b5 = read(test_blow5)
    assert b5.getCalibrationScale(readidstarget[read_idx]) == (read_channel_attrs_r['range'] / read_channel_attrs_r['digitisation'])
    b5.close()

def test_blow5_signal():
    b5 = read(test_blow5)
    assert (b5.getSignal(readidstarget[read_idx])[:10] == signal_r_first10).all()
    assert (b5.getSignal(readidstarget[read_idx])[-10:] == signal_r_last10).all()
    assert len(b5.getSignal(readidstarget[read_idx])) == read_raw_attrs_r['duration']
    b5.close()

def test_blow5_pASignal():
    b5 = read(test_blow5)
    assert np.isclose(b5.getpASignal(readidstarget[read_idx])[:10], pASignal_r_first10).all()
    assert np.isclose(b5.getpASignal(readidstarget[read_idx])[-10:], pASignal_r_last10).all()
    assert len(b5.getpASignal(readidstarget[read_idx])) == read_raw_attrs_r['duration']
    b5.close()

def test_blow5_normSignal():
    b5 = read(test_blow5)
    assert np.isclose(b5.getZNormSignal(readidstarget[read_idx])[:10], normSignal_r_first10).all()
    assert np.isclose(b5.getZNormSignal(readidstarget[read_idx])[-10:], normSignal_r_last10).all()
    assert len(b5.getZNormSignal(readidstarget[read_idx])) == read_raw_attrs_r['duration']
    b5.close()

def test_blow5_channel_number():
    b5 = read(test_blow5)
    assert b5.getChannelNumber(readidstarget[read_idx]) == int(read_channel_attrs_r['channel_number'])
    b5.close()

def test_blow5_start_time():
    b5 = read(test_blow5)
    assert b5.getStartTime(readidstarget[read_idx]) == read_raw_attrs_r['start_time']
    b5.close()

def test_blow5_sampling_rate():
    b5 = read(test_blow5)
    assert b5.getSamplingRate(readidstarget[read_idx]) == read_channel_attrs_r['sampling_rate']
    b5.close()

def test_blow5_start_time_in_minutes():
    b5 = read(test_blow5)
    assert b5.getStartTimeInMinutes(readidstarget[read_idx]) == start_time_in_min_r
    b5.close()

def test_blow5_file_version():
    b5 = read(test_blow5)
    assert b5.getFileVersion() == slow5_blow5_file_version
    b5.close()

def test_blow5_pore_type():
    b5 = read(test_blow5)
    assert b5.getPoreType() == read_attrs_r['pore_type'].decode('utf-8')
    b5.close()

def test_blow5_run_id():
    b5 = read(test_blow5)
    assert b5.getRunID() == read_tracking_attrs_r['run_id'].decode('utf-8')
    b5.close()

def test_blow5_duration():
    b5 = read(test_blow5)
    assert b5.getDuration(readidstarget[read_idx]) == read_raw_attrs_r['duration']
    b5.close()

def test_blow5_end_reason():
    b5 = read(test_blow5)
    assert b5.getEndReason(readidstarget[read_idx]) == read_raw_attrs_r['end_reason']
    b5.close()

def test_blow5_median_before():
    b5 = read(test_blow5)
    assert np.isclose(b5.getMedianBefore(readidstarget[read_idx]), read_raw_attrs_r['median_before'])
    b5.close()

def test_blow5_number():
    b5 = read(test_blow5)
    assert b5.getReadNumber(readidstarget[read_idx]) == read_raw_attrs_r['read_number']
    b5.close()

def test_blow5_start_mux():
    b5 = read(test_blow5)
    assert b5.getStartMux(readidstarget[read_idx]) == read_raw_attrs_r['start_mux']
    b5.close()

def test_blow5_start_time():
    b5 = read(test_blow5)
    assert b5.getStartTime(readidstarget[read_idx]) == read_raw_attrs_r['start_time']
    b5.close()

def test_blow5_channel_number():
    b5 = read(test_blow5)
    assert b5.getChannelNumber(readidstarget[read_idx]) == int(read_channel_attrs_r['channel_number'])
    b5.close()

def test_blow5_barcoding_enabled():
    b5 = read(test_blow5)
    assert b5.isBarcodingEnabled() == bool(int(read_context_attrs_r['barcoding_enabled']))
    b5.close()

def test_blow5_experiment_duration():
    b5 = read(test_blow5)
    assert b5.getExperimentDurationSet() == int(read_context_attrs_r['experiment_duration_set'])
    b5.close()

def test_blow5_experiment_type():
    b5 = read(test_blow5)
    assert b5.getExperimentType() == read_context_attrs_r['experiment_type'].decode('utf-8')
    b5.close()

def test_blow5_local_basecalled():
    b5 = read(test_blow5)
    assert b5.isLocalBasecalled() == bool(int(read_context_attrs_r['local_basecalling']))
    b5.close()

def test_blow5_package():
    b5 = read(test_blow5)
    assert b5.getPackage() == read_context_attrs_r['package'].decode('utf-8')
    b5.close()

def test_blow5_package_version():
    b5 = read(test_blow5)
    assert b5.getPackageVersion() == read_context_attrs_r['package_version'].decode('utf-8')
    b5.close()

def test_blow5_sequencing_kit():
    b5 = read(test_blow5)
    assert b5.getSequencingKit() == read_context_attrs_r['sequencing_kit'].decode('utf-8')
    b5.close()

def test_blow5_asic_id():
    b5 = read(test_blow5)
    assert b5.getAsicID() == read_tracking_attrs_r['asic_id'].decode('utf-8')
    b5.close()

def test_blow5_asic_eeprom():
    b5 = read(test_blow5)
    assert b5.getAsicIDEeprom() == read_tracking_attrs_r['asic_id_eeprom'].decode('utf-8')
    b5.close()

def test_blow5_asic_temp():
    b5 = read(test_blow5)
    assert b5.getAsicTemp() == float(read_tracking_attrs_r['asic_temp'])
    b5.close()

def test_blow5_asic_version():
    b5 = read(test_blow5)
    assert b5.getAsicVersion() == read_tracking_attrs_r['asic_version'].decode('utf-8')
    b5.close()

def test_blow5_auto_update():
    b5 = read(test_blow5)
    assert b5.isAutoUpdated() == bool(int(read_tracking_attrs_r['auto_update']))
    b5.close()

def test_blow5_auto_update_source():
    b5 = read(test_blow5)
    assert b5.getAutoUpdateSource() == read_tracking_attrs_r['auto_update_source'].decode('utf-8')
    b5.close()

def test_blow5_bream_standard():
    b5 = read(test_blow5)
    assert b5.isBreamStandard() == bool(int(read_tracking_attrs_r['bream_is_standard']))
    b5.close()

def test_blow5_config_version():
    b5 = read(test_blow5)
    assert b5.getConfigurationVersion() == read_tracking_attrs_r['configuration_version'].decode('utf-8')
    b5.close()

def test_blow5_device_id():
    b5 = read(test_blow5)
    assert b5.getDeviceID() == read_tracking_attrs_r['device_id'].decode('utf-8')
    b5.close()

def test_blow5_device_type():
    b5 = read(test_blow5)
    assert b5.getDeviceType() == read_tracking_attrs_r['device_type'].decode('utf-8')
    b5.close()

def test_blow5_distribution_status():
    b5 = read(test_blow5)
    assert b5.getDistributionStatus() == read_tracking_attrs_r['distribution_status'].decode('utf-8')
    b5.close()

def test_blow5_distribution_version():
    b5 = read(test_blow5)
    assert b5.getDistributionVersion() == read_tracking_attrs_r['distribution_version'].decode('utf-8')
    b5.close()

def test_blow5_exp_script_name():
    b5 = read(test_blow5)
    assert b5.getExpScriptPurpose() == read_tracking_attrs_r['exp_script_purpose'].decode('utf-8')
    b5.close()

def test_blow5_exp_time_start():
    b5 = read(test_blow5)
    assert b5.getExpStartTime() == read_tracking_attrs_r['exp_start_time'].decode('utf-8')
    b5.close()

def test_blow5_flow_cell():
    b5 = read(test_blow5)
    assert b5.getFlowCellID() == read_tracking_attrs_r['flow_cell_id'].decode('utf-8')
    b5.close()

def test_blow5_flow_cell_product():
    b5 = read(test_blow5)
    assert b5.getFlowCellProductCode() == read_tracking_attrs_r['flow_cell_product_code'].decode('utf-8')
    b5.close()

def test_blow5_guppy_version():
    b5 = read(test_blow5)
    assert b5.getGuppyVersion() == read_tracking_attrs_r['guppy_version'].decode('utf-8')
    b5.close()

def test_blow5_heat_sink():
    b5 = read(test_blow5)
    assert b5.getHeatSinkTemp() == float(read_tracking_attrs_r['heatsink_temp'])
    b5.close()

def test_blow5_host_product_code():
    b5 = read(test_blow5)
    assert b5.getHostProductCode() == read_tracking_attrs_r['host_product_code'].decode('utf-8')
    b5.close()

def test_blow5_host_product_number():
    b5 = read(test_blow5)
    assert b5.getHostProductSerialNumber() == read_tracking_attrs_r['host_product_serial_number'].decode('utf-8')
    b5.close()

def test_blow5_hostname():
    b5 = read(test_blow5)
    assert b5.getHostname() == read_tracking_attrs_r['hostname'].decode('utf-8')
    b5.close()

def test_blow5_installation_type():
    b5 = read(test_blow5)
    assert b5.getInstallationType() == read_tracking_attrs_r['installation_type'].decode('utf-8')
    b5.close()

def test_blow5_local_firmware_file():
    b5 = read(test_blow5)
    assert b5.getLocalFirmwareFile() == int(read_tracking_attrs_r['local_firmware_file'])
    b5.close()

def test_blow5_os():
    b5 = read(test_blow5)
    assert b5.getOperatingSystem() == read_tracking_attrs_r['operating_system'].decode('utf-8')
    b5.close()

def test_blow5_prot_goup_id():
    b5 = read(test_blow5)
    assert b5.getProtocolGroupID() == read_tracking_attrs_r['protocol_group_id'].decode('utf-8')
    b5.close()

def test_blow5_prot_run_id():
    b5 = read(test_blow5)
    assert b5.getProtocolRunID() == read_tracking_attrs_r['protocol_run_id'].decode('utf-8')
    b5.close()

def test_blow5_prot_start_time():
    b5 = read(test_blow5)
    assert b5.getProtocolStartTime() == read_tracking_attrs_r['protocol_start_time'].decode('utf-8')
    b5.close()

def test_blow5_prot_version():
    b5 = read(test_blow5)
    assert b5.getProtocolVersion() == read_tracking_attrs_r['protocols_version'].decode('utf-8')
    b5.close()

def test_blow5_run_id():
    b5 = read(test_blow5)
    assert b5.getRunID() == read_tracking_attrs_r['run_id'].decode('utf-8')
    b5.close()

def test_blow5_sample_id():
    b5 = read(test_blow5)
    assert b5.getSampleID() == read_tracking_attrs_r['sample_id'].decode('utf-8')
    b5.close()

def test_blow5_usb():
    b5 = read(test_blow5)
    assert b5.getUSBConfig() == read_tracking_attrs_r['usb_config'].decode('utf-8')
    b5.close()

def test_blow5_version():
    b5 = read(test_blow5)
    assert b5.getVersion() == read_tracking_attrs_r['version'].decode('utf-8')
    b5.close()

# ============================================================================================
# Tests for pod5

pod5_file_version = '0.1.7'
pod5_end_reason = 4

def test_pod5_opens():
    p5 = read(test_pod5)
    assert p5.isOpen()
    p5.close()
    assert not p5.isOpen()

def test_pod5_ids():
    p5 = read(test_pod5)
    assert set(p5.getReads()) == set(readidstarget)
    p5.close()

def test_pod5_getitem_with_iter():
    p5 = read(test_pod5)
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
    p5 = read(test_pod5)
    for readid, target in zip(p5, readidstarget):
        assert readid == target
    p5.close()

def test_pod5_offset():
    p5 = read(test_pod5)
    assert p5.getOffset(readidstarget[read_idx]) == read_channel_attrs_r['offset']
    p5.close()

def test_pod5_calibration_scale():
    p5 = read(test_pod5)
    assert p5.getCalibrationScale(readidstarget[read_idx]) == read_channel_attrs_r['range'] / read_channel_attrs_r['digitisation']
    p5.close()

def test_pod5_signal():
    p5 = read(test_pod5)
    assert (p5.getSignal(readidstarget[read_idx])[:10] == signal_r_first10).all()
    assert (p5.getSignal(readidstarget[read_idx])[-10:] == signal_r_last10).all()
    assert len(p5.getSignal(readidstarget[read_idx])) == read_raw_attrs_r['duration']
    p5.close()

def test_pod5_pASignal():
    p5 = read(test_pod5)
    assert np.isclose(p5.getpASignal(readidstarget[read_idx])[:10], pASignal_r_first10).all()
    assert np.isclose(p5.getpASignal(readidstarget[read_idx])[-10:], pASignal_r_last10).all()
    assert len(p5.getpASignal(readidstarget[read_idx])) == read_raw_attrs_r['duration']
    p5.close()

def test_pod5_normSignal():
    p5 = read(test_pod5)
    assert np.isclose(p5.getZNormSignal(readidstarget[read_idx])[:10], normSignal_r_first10).all()
    assert np.isclose(p5.getZNormSignal(readidstarget[read_idx])[-10:], normSignal_r_last10).all()
    assert len(p5.getZNormSignal(readidstarget[read_idx])) == read_raw_attrs_r['duration']
    p5.close()

def test_pod5_channel_number():
    p5 = read(test_pod5)
    assert p5.getChannelNumber(readidstarget[read_idx]) == int(read_channel_attrs_r['channel_number'])
    p5.close()

def test_pod5_sampling_rate():
    p5 = read(test_pod5)
    assert p5.getSamplingRate(readidstarget[read_idx]) == read_channel_attrs_r['sampling_rate']
    p5.close()
    
def test_pod5_start_time():
    p5 = read(test_pod5)
    assert p5.getStartTime(readidstarget[read_idx]) == read_raw_attrs_r['start_time']
    p5.close()

def test_pod5_start_time_in_minutes():
    p5 = read(test_pod5)
    assert p5.getStartTimeInMinutes(readidstarget[read_idx]) == start_time_in_min_r
    p5.close()

def test_pod5_file_version():
    p5 = read(test_pod5)
    assert p5.getFileVersion() == pod5_file_version
    p5.close()

def test_pod5_pore_type():
    p5 = read(test_pod5)
    assert p5.getPoreType(readidstarget[read_idx]) == read_attrs_r['pore_type'].decode('utf-8')
    p5.close()

def test_pod5_run_id():
    p5 = read(test_pod5)
    assert p5.getRunID(readidstarget[read_idx]) == read_tracking_attrs_r['run_id'].decode('utf-8')
    p5.close()

def test_pod5_duration():
    p5 = read(test_pod5)
    assert p5.getDuration(readidstarget[read_idx]) == read_raw_attrs_r['duration']
    p5.close()

def test_pod5_end_reason():
    p5 = read(test_pod5)
    assert p5.getEndReason(readidstarget[read_idx]) == pod5_end_reason
    p5.close()

def test_pod5_median_before():
    p5 = read(test_pod5)
    assert p5.getMedianBefore(readidstarget[read_idx]) == read_raw_attrs_r['median_before']
    p5.close()

def test_pod5_minknow_events():
    p5 = read(test_pod5)
    assert p5.getNumMinknowEvents(readidstarget[read_idx]) == read_raw_attrs_r['num_minknow_events']
    p5.close()

def test_pod5_reads_since_mux_change():
    p5 = read(test_pod5)
    assert p5.getNumReadsSinceMuxChange(readidstarget[read_idx]) == read_raw_attrs_r['num_reads_since_mux_change']
    p5.close()

def test_pod5_predicted_scaling():
    p5 = read(test_pod5)
    assert np.isnan(p5.getPredictedScaling(readidstarget[read_idx])).all()
    p5.close()

def test_pod5_number():
    p5 = read(test_pod5)
    assert p5.getReadNumber(readidstarget[read_idx]) == read_raw_attrs_r['read_number']
    p5.close()

# def test_pod5_start_mux():
#     p5 = open(test_fast5)
#     assert p5.getStartMux(readidstarget[read_idx]) == read_raw_attrs_r['start_mux']
#     p5.close()

def test_pod5_start_time():
    p5 = read(test_pod5)
    assert p5.getStartTime(readidstarget[read_idx]) == read_raw_attrs_r['start_time']
    p5.close()

def test_pod5_time_since_mux_change():
    p5 = read(test_pod5)
    assert np.isclose(p5.getTimeSinceMuxChange(readidstarget[read_idx]), 155.00896)
    p5.close()

def test_pod5_channel_number():
    p5 = read(test_pod5)
    assert p5.getChannelNumber(readidstarget[read_idx]) == int(read_channel_attrs_r['channel_number'])
    p5.close()

def test_pod5_barcoding_enabled():
    p5 = read(test_pod5)
    assert p5.isBarcodingEnabled(readidstarget[read_idx]) == bool(int(read_context_attrs_r['barcoding_enabled']))
    p5.close()

def test_pod5_experiment_duration():
    p5 = read(test_pod5)
    assert p5.getExperimentDurationSet(readidstarget[read_idx]) == int(read_context_attrs_r['experiment_duration_set'])
    p5.close()

def test_pod5_experiment_type():
    p5 = read(test_pod5)
    assert p5.getExperimentType(readidstarget[read_idx]) == read_context_attrs_r['experiment_type'].decode('utf-8')
    p5.close()

def test_pod5_local_basecalled():
    p5 = read(test_pod5)
    assert p5.isLocalBasecalled(readidstarget[read_idx]) == bool(int(read_context_attrs_r['local_basecalling']))
    p5.close()

def test_pod5_package():
    p5 = read(test_pod5)
    assert p5.getPackage(readidstarget[read_idx]) == read_context_attrs_r['package'].decode('utf-8')
    p5.close()

def test_pod5_package_version():
    p5 = read(test_pod5)
    assert p5.getPackageVersion(readidstarget[read_idx]) == read_context_attrs_r['package_version'].decode('utf-8')
    p5.close()

def test_pod5_sequencing_kit():
    p5 = read(test_pod5)
    assert p5.getSequencingKit(readidstarget[read_idx]) == read_context_attrs_r['sequencing_kit'].decode('utf-8')
    p5.close()

def test_pod5_asic_id():
    p5 = read(test_pod5)
    assert p5.getAsicID(readidstarget[read_idx]) == read_tracking_attrs_r['asic_id'].decode('utf-8')
    p5.close()

def test_pod5_asic_eeprom():
    p5 = read(test_pod5)
    assert p5.getAsicIDEeprom(readidstarget[read_idx]) == read_tracking_attrs_r['asic_id_eeprom'].decode('utf-8')
    p5.close()

def test_pod5_asic_temp():
    p5 = read(test_pod5)
    assert p5.getAsicTemp(readidstarget[read_idx]) == float(read_tracking_attrs_r['asic_temp'])
    p5.close()

def test_pod5_asic_version():
    p5 = read(test_pod5)
    assert p5.getAsicVersion(readidstarget[read_idx]) == read_tracking_attrs_r['asic_version'].decode('utf-8')
    p5.close()

def test_pod5_auto_update():
    p5 = read(test_pod5)
    assert p5.isAutoUpdated(readidstarget[read_idx]) == bool(int(read_tracking_attrs_r['auto_update']))
    p5.close()

def test_pod5_auto_update_source():
    p5 = read(test_pod5)
    assert p5.getAutoUpdateSource(readidstarget[read_idx]) == read_tracking_attrs_r['auto_update_source'].decode('utf-8')
    p5.close()

def test_pod5_bream_standard():
    p5 = read(test_pod5)
    assert p5.isBreamStandard(readidstarget[read_idx]) == bool(int(read_tracking_attrs_r['bream_is_standard']))
    p5.close()

def test_pod5_config_version():
    p5 = read(test_pod5)
    assert p5.getConfigurationVersion(readidstarget[read_idx]) == read_tracking_attrs_r['configuration_version'].decode('utf-8')
    p5.close()

def test_pod5_device_id():
    p5 = read(test_pod5)
    assert p5.getDeviceID(readidstarget[read_idx]) == read_tracking_attrs_r['device_id'].decode('utf-8')
    p5.close()

def test_pod5_device_type():
    p5 = read(test_pod5)
    assert p5.getDeviceType(readidstarget[read_idx]) == read_tracking_attrs_r['device_type'].decode('utf-8')
    p5.close()

def test_pod5_distribution_status():
    p5 = read(test_pod5)
    assert p5.getDistributionStatus(readidstarget[read_idx]) == read_tracking_attrs_r['distribution_status'].decode('utf-8')
    p5.close()

def test_pod5_distribution_version():
    p5 = read(test_pod5)
    assert p5.getDistributionVersion(readidstarget[read_idx]) == read_tracking_attrs_r['distribution_version'].decode('utf-8')
    p5.close()

def test_pod5_exp_script_name():
    p5 = read(test_pod5)
    assert p5.getExpScriptPurpose(readidstarget[read_idx]) == read_tracking_attrs_r['exp_script_purpose'].decode('utf-8')
    p5.close()

def test_pod5_exp_time_start():
    p5 = read(test_pod5)
    assert p5.getExpStartTime(readidstarget[read_idx]) == read_tracking_attrs_r['exp_start_time'].decode('utf-8')
    p5.close()

def test_pod5_flow_cell():
    p5 = read(test_pod5)
    assert p5.getFlowCellID(readidstarget[read_idx]) == read_tracking_attrs_r['flow_cell_id'].decode('utf-8')
    p5.close()

def test_pod5_flow_cell_product():
    p5 = read(test_pod5)
    assert p5.getFlowCellProductCode(readidstarget[read_idx]) == read_tracking_attrs_r['flow_cell_product_code'].decode('utf-8')
    p5.close()

def test_pod5_guppy_version():
    p5 = read(test_pod5)
    assert p5.getGuppyVersion(readidstarget[read_idx]) == read_tracking_attrs_r['guppy_version'].decode('utf-8')
    p5.close()

def test_pod5_heat_sink():
    p5 = read(test_pod5)
    assert p5.getHeatSinkTemp(readidstarget[read_idx]) == float(read_tracking_attrs_r['heatsink_temp'])
    p5.close()

def test_pod5_host_product_code():
    p5 = read(test_pod5)
    assert p5.getHostProductCode(readidstarget[read_idx]) == read_tracking_attrs_r['host_product_code'].decode('utf-8')
    p5.close()

def test_pod5_host_product_number():
    p5 = read(test_pod5)
    assert p5.getHostProductSerialNumber(readidstarget[read_idx]) == read_tracking_attrs_r['host_product_serial_number'].decode('utf-8')
    p5.close()

def test_pod5_hostname():
    p5 = read(test_pod5)
    assert p5.getHostname(readidstarget[read_idx]) == read_tracking_attrs_r['hostname'].decode('utf-8')
    p5.close()

def test_pod5_installation_type():
    p5 = read(test_pod5)
    assert p5.getInstallationType(readidstarget[read_idx]) == read_tracking_attrs_r['installation_type'].decode('utf-8')
    p5.close()

def test_pod5_local_firmware_file():
    p5 = read(test_pod5)
    assert p5.getLocalFirmwareFile(readidstarget[read_idx]) == int(read_tracking_attrs_r['local_firmware_file'])
    p5.close()

def test_pod5_os():
    p5 = read(test_pod5)
    assert p5.getOperatingSystem(readidstarget[read_idx]) == read_tracking_attrs_r['operating_system'].decode('utf-8')
    p5.close()

def test_pod5_prot_goup_id():
    p5 = read(test_pod5)
    assert p5.getProtocolGroupID(readidstarget[read_idx]) == read_tracking_attrs_r['protocol_group_id'].decode('utf-8')
    p5.close()

def test_pod5_prot_run_id():
    p5 = read(test_pod5)
    assert p5.getProtocolRunID(readidstarget[read_idx]) == read_tracking_attrs_r['protocol_run_id'].decode('utf-8')
    p5.close()

def test_pod5_prot_start_time():
    p5 = read(test_pod5)
    assert p5.getProtocolStartTime(readidstarget[read_idx]) == read_tracking_attrs_r['protocol_start_time'].decode('utf-8')
    p5.close()

def test_pod5_prot_version():
    p5 = read(test_pod5)
    assert p5.getProtocolVersion(readidstarget[read_idx]) == read_tracking_attrs_r['protocols_version'].decode('utf-8')
    p5.close()

def test_pod5_run_id():
    p5 = read(test_pod5)
    assert p5.getRunID(readidstarget[read_idx]) == read_tracking_attrs_r['run_id'].decode('utf-8')
    p5.close()

def test_pod5_sample_id():
    p5 = read(test_pod5)
    assert p5.getSampleID(readidstarget[read_idx]) == read_tracking_attrs_r['sample_id'].decode('utf-8')
    p5.close()

def test_pod5_usb():
    p5 = read(test_pod5)
    assert p5.getUSBConfig(readidstarget[read_idx]) == read_tracking_attrs_r['usb_config'].decode('utf-8')
    p5.close()

def test_pod5_version():
    p5 = read(test_pod5)
    assert p5.getVersion(readidstarget[read_idx]) == read_tracking_attrs_r['version'].decode('utf-8')
    p5.close()