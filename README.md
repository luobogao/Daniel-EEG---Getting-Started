
# EEG Data Analysis with MNE-Python

## Overview
This project demonstrates how to easily dive into EEG data using Python with the MNE library. The Cognionics system records data in a standard format, including .EEG, .VHDR, and .VMRK files, which MNE is adept at loading. We'll start by plotting the data and then explore various analysis methods.

## File Types
- **.EEG**: Contains the voltages from each sensor at every recording interval. With the Cognionics system recording at 500 Hz, each row is 2 milliseconds apart.
- **.VHDR**: Provides general information about the recording, including the filenames of the .EEG and .VMRK files. Filenames can be manually edited if necessary.
- **.VMRK**: Includes timestamped 'events', each with a label and time in milliseconds. These are based on spoken notes provided during the session and have been pre-added.

## Timestamps File
Daniel recorded observations during the EEG session, noting his experiences while minimizing movement. The Timestamps CSV file aligns these observations with the EEG data, highlighting key moments such as 'fruitions'.

## Installation
```bash
pip install mne
```

## Loading Data
```python
import mne

file_path = "Aug_20.vhdr"
raw = mne.io.read_raw_brainvision(file_path, preload=True)
events, event_ids = mne.events_from_annotations(raw)
fig = raw.plot(events=events, event_id=event_ids, block=True)
fig.show()
```

## Using the Plot
The default plot provides a comprehensive view of voltage levels over time, with the ability to scroll through timestamps. Events are marked with vertical lines. Specific points, like Daniel's 'fruitions', are clearly indicated, allowing for precise examination despite potential data interference from facial movements.

## Further Analysis
Further analysis requires selecting specific electrodes and choosing the appropriate analytical approach to explore the nuances of events such as 'fruitions'.

## Note on VHDR File
Ensure the VHDR file correctly references the associated .EEG and .VMRK files to avoid loading issues. Here's a sample header from a .VHDR file:
```
Codepage=UTF-8
DataFile=Aug_20.eeg
MarkerFile=Aug_20.vmrk
DataFormat=BINARY
DataOrientation=MULTIPLEXED
DataType=TIMEDOMAIN
NumberOfChannels=26
DataPoints=958464
SamplingInterval=2000
```
