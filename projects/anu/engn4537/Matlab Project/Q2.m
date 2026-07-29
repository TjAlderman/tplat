close all
clear workspace

% create an audiorecorder object with the correct fs and resolution
mic = audiorecorder(48000,16,1);

% take a 12 second recording
record(mic);
pause(12);
stop(mic);

% get the recording data
recording = getaudiodata(mic);

% play the recording
clip = audioplayer(recording,48000,16);
play(clip);

% write recording to wav
audiowrite("Results/DSP_TimothyAlder2.wav",recording,48000);