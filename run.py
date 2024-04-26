import mne

# Load the EEG data
file_path = 'Aug_20.vhdr'  # Update this path to where your .vhdr file is located

raw = mne.io.read_raw_brainvision(file_path, preload=True)

# Extract events from annotations
events, event_ids = mne.events_from_annotations(raw)

# Pick the P4 electrode
p4_data = raw.copy().pick_channels(['P4'])

# Plot the raw data of P4 with event markers
fig =raw.plot(events=events, event_id=event_ids, block=True)

# Show the plot
fig.show()
