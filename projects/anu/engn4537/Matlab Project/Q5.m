close all
clear workspace

% Question 5.1

% load in the signals
x_t = audioread("Results/DSP_TimothyAlder.wav");
t = [0:1/48000:size(x_t,1)/48000-1/48000];
figure(1)
plot(t,x_t);
xlim([0,size(x_t,1)/48000-1/48000]);

% compute their fourier transforms using fft
x_k = dft2(x_t.',48000);

% plot the result
% adjusting plot parameters
title('DFT of DSP_TimothyAlder.wav using dft2 function', 'Interpreter', 'none');

% Question 5.2

% load in the signals
x_t = audioread("Resource Files/DSP_Noise.wav");

% compute their fourier transforms using fft
x_k = dft2(x_t.',48000);

% plot the result
% adjusting plot parameters
title('DFT of DSP_Noise.wav using dft2 function', 'Interpreter', 'none');

% Question 5.4
[x_t Fs] = audioread("Results/DSP_TimothyAlder.wav");

time_steps = 32; % Number of desired separate intervals of x_t
WINDOW = size(x_t,1)/time_steps; % Corresponding window size
NOVERLAP = 0; % Overlap between windows

figure(4);
spectrogram(x_t,WINDOW,NOVERLAP,[],Fs,'yaxis');
title('Timothy Alder')
[S,F,T] = spectrogram(x_t,WINDOW,NOVERLAP,[],Fs,'yaxis');

figure(5);
waterplot(S,F,T)
title('Waterplot of Timothy Alder Spectrogram')

% Question 5.8
x_t = audioread("Results/DSP_TimothyAlder.wav");
[y_t StartTime] = FindSignalStart(x_t);
[y_t EndTime] = FindSignalStop(y_t);
audiowrite('Results/DSP_Chopped_TimothyAlder.wav',y_t,48000);

time_steps = 32; % Number of desired separate intervals of x_t
WINDOW = size(y_t,1)/time_steps; % Corresponding window size
NOVERLAP = 0; % Overlap between windows
figure(6);
spectrogram(y_t,WINDOW,NOVERLAP,[],Fs,'yaxis');
title('Timothy Alder Chopped')

function waterplot(s,f,t)
% Waterfall plot of spectrogram
    waterfall(f,t,abs(s)'.^2)
    set(gca,XDir="reverse",View=[30 50])
    xlabel("Frequency (Hz)")
    ylabel("Time (s)")
end