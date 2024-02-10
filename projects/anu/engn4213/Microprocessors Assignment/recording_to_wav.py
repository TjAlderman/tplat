import numpy as np
import soundfile as sf
import pandas as pd
from pathlib import Path
from re import search
import matplotlib.pyplot as plt

raw_data = {}

# loading in data
p = Path('/Users/timothyalder/Documents/ANU/ENGN4213/Microprocessors Assignment')
file = list(p.glob('*.txt'))
freq_files = []
for f in file:
    # get FFT data (for debugging)
    if search('freq',f.name) != None:
        file.remove(f)
        freq_files.append(f)
# get microphone output data (to convert to .wav)
for i in range(len(file)):
    data = pd.read_csv(str(file[i]), sep=',', header = None)
    data = data.transpose()
    data = data[0:len(data-1)]
    # normalise from -1 to 1
    raw_data[file[i].name] = data
    min = data.min()
    data = data-min
    max = data.max()
    data = (data/max)*2
    data = data-1

    # creating a time index from the sampling freq
    sampling_freq = 2000
    total_time = len(data)/sampling_freq
    time_space = np.linspace(0,total_time,len(data))

    #plt.plot(time_space,raw_data[file[i].name])
    #plt.show()

    # save as a .wav file
    recording_name = file[i].name.replace('.txt','')
    sf.write(f'{recording_name}.wav', data, sampling_freq)


