close all
clear workspace

% Question 1.1
audioinfo("Resource Files/DSP_Speech.wav")

% Question 1.2
DSP_Speech = audioread("Resource Files/DSP_Speech.wav", [64000 144000]);

% Question 1.3
clip = audioplayer(DSP_Speech, 16000, 16);
play(clip)

% Question 1.4
pause(1);
stop(clip)