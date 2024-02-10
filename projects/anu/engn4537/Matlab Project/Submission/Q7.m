% Question 7
close all
clear

% read in DSP_Music.wav
[x_t Fs] = audioread("Resource Files/DSP_Music.wav");
% keep only the first  channel
x_t = x_t(:,1);

% define a corresponding t-space vector
t_space = [0:1/Fs:size(x_t,1)/Fs-1/Fs].';

% modulate the signal
x_t_AM = sin((9000*(2*pi)).*t_space).*x_t;
% t_space = t_space(1:Fs*52);
% x_t_AM = x_t_AM(1:Fs*52);

% % play the result
% clip = audioplayer(x_t_AM, Fs);
% play(clip)
% pause(5)
% stop(clip)

% Question 7.1.1

% Generating plots for the AM signal
figure(1);
subplot(1,3,1);
plot(t_space,x_t_AM);
xlim([0,t_space(end)])
title('DSP_Music.wav Amplitude Modulated', 'Interpreter', 'none');
xlabel('Time (s)');
ylabel('|x_{AM}(t)|');

% Perform DFT of the AM signal
x_k_AM = fft(x_t_AM.');
x_k_AM = x_k_AM*2/size(x_t_AM,1);
freq_res = Fs/size(x_t_AM,1);
adj_k_space = [0:freq_res:Fs/2-freq_res];

% Plot magnitude of DFT
subplot(1,3,2);
stem(adj_k_space,abs(x_k_AM(1:size(adj_k_space,2))))
xlabel('K-space (Hz)')
ylabel('|X(K)|')
title('X(K) versus K')
xlim([0,Fs/2])

phase_space = [0:pi/size(x_k_AM,2):pi-pi/size(x_k_AM,2)];

% Plot phase of DFT
subplot(1,3,3);
plot(phase_space,unwrap(angle(x_k_AM)))
desired_ticks = [pi/4, pi/2, 3*pi/4, pi];
xticks(desired_ticks);
xticklabels({'\pi/4', '\pi/2', '3\pi/4', '\pi'});
xlabel('{\omega} (rads)')
ylabel('Arg{X(K)}')
title('Arg{X(K)} versus {\omega}')
xlim([0,pi])

% Generating plots for the original signal
figure(2);
subplot(1,3,1);
plot(t_space,x_t);
xlim([0,t_space(end)])
title('DSP_Music.wav', 'Interpreter', 'none');
xlabel('Time (s)');
ylabel('|x(t)|');

% Perform DFT of the original signal
x_k = fft(x_t.');
x_k = x_k*2/size(x_t,1);
freq_res = Fs/size(x_t,1);
adj_k_space = [0:freq_res:Fs/2-freq_res];

% Plot magnitude of the DFT
subplot(1,3,2);
stem(adj_k_space,abs(x_k(1:size(adj_k_space,2))))
xlabel('K-space (Hz)')
ylabel('|X(K)|')
title('X(K) versus K')
xlim([0,Fs/2])

phase_res = pi/(size(x_k,2)/2);
phase_space = [0:phase_res:pi-phase_res];

% Plot phase of the DFT
subplot(1,3,3);
plot(phase_space,unwrap(angle(x_k(1:end/2))))
desired_ticks = [pi/4, pi/2, 3*pi/4, pi];
xticks(desired_ticks);
xticklabels({'\pi/4', '\pi/2', '3\pi/4', '\pi'});
xlabel('{\omega} (rads)')
ylabel('Arg{X(K)}')
title('Arg{X(K)} versus {\omega}')
xlim([0,pi])

% Generating plots for symmetrical DFT of the original signal
figure(3);
subplot(1,3,1);
plot(t_space,x_t);
xlim([0,t_space(end)])
title('DSP_Music.wav', 'Interpreter', 'none');
xlabel('Time (s)');
ylabel('|x(t)|');

% perform DFT
x_k = fft(x_t.');
x_k = x_k/size(x_t,1);
x_k = circshift(x_k,size(x_k,2)/2);
freq_res = Fs/size(x_t,1);
adj_k_space = [-(Fs/2-freq_res):freq_res:Fs/2];

% Plot magnitude of the DFT
subplot(1,3,2);
stem(adj_k_space,abs(x_k))
xlabel('K-space (Hz)')
ylabel('|X(K)|')
title('X(K) versus K')
xlim([-Fs/2,Fs/2])

phase_res = pi/(size(x_k,2)/2);
phase_space = [-(pi-phase_res):phase_res:pi];

% Plot phase of the DFT
subplot(1,3,3);
plot(phase_space,unwrap(angle(x_k)))
desired_ticks = [-pi, -pi/2, 0, pi/2, pi];
xticks(desired_ticks);
xticklabels({'-\pi', '\pi/2', '0', '\pi//2', '\pi'});
xlabel('{\omega} (rads)')
ylabel('Arg{X(K)}')
title('Arg{X(K)} versus {\omega}')
xlim([-pi,pi])

% Question 7.1.2

t_space = [0:(1/Fs):((size(x_t,1)-1)/Fs)];
AM = sin(2*pi*9000*t_space);

% Generating plots for the modulation signal
figure(4);
subplot(1,3,1);
plot(t_space,AM);
xlim([0,2/900])
title('Some Periods of the AM Signal', 'Interpreter', 'none');
xlabel('Time (s)');
ylabel('|x(t)|');

% Perform DFT of the modulation signal
x_k_mod = fft(AM);
x_k_mod = x_k_mod*2/size(AM,2);
freq_res = Fs/size(AM,2);
adj_k_space = [0:freq_res:Fs/2];

% Plot magnitude of the DFT
subplot(1,3,2);
stem(adj_k_space,abs(x_k_mod(1:size(adj_k_space,2))))
xlabel('K-space (Hz)')
ylabel('|X(K)|')
title('X(K) versus K')
xlim([0,Fs/2])

phase_res = pi/(size(x_k_mod,2)/2);
phase_space = [0:phase_res:pi-phase_res];

% Plot phase of DFT
subplot(1,3,3);
plot(phase_space,unwrap(angle(x_k_mod(1:end/2))))
desired_ticks = [pi/4, pi/2, 3*pi/4, pi];
xticks(desired_ticks);
xticklabels({'\pi/4', '\pi/2', '3\pi/4', '\pi'});
xlabel('{\omega} (rads)')
ylabel('Arg{X(K)}')
title('Arg{X(K)} versus {\omega}')
xlim([0,pi])

t_space = [0:(1/Fs):((size(x_t,1)-1)/Fs)];
AM = sin(2*pi*9000*t_space);
t_space = t_space(1:52*Fs);
AM = AM(1:52*Fs);

% Generating plots for the clipped modulation signal (without spectral
% leakage)
figure(5);
subplot(1,3,1);
plot(t_space,AM);
xlim([0,2/900])
title('Some Periods of the AM Signal', 'Interpreter', 'none');
xlabel('Time (s)');
ylabel('|x(t)|');

% Perform DFT of the modulation signal
x_k_mod = fft(AM);
x_k_mod = x_k_mod*2/size(AM,2);
freq_res = Fs/size(AM,2);
adj_k_space = [0:freq_res:Fs/2];

% Plot magnitude of the DFT
subplot(1,3,2);
stem(adj_k_space,abs(x_k_mod(1:size(adj_k_space,2))))
xlabel('K-space (Hz)')
ylabel('|X(K)|')
title('X(K) versus K')
xlim([0,Fs/2])

phase_res = pi/(size(x_k_mod,2)/2);
phase_space = [0:phase_res:pi-phase_res];

% Plot phase of DFT
subplot(1,3,3);
plot(phase_space,unwrap(angle(x_k_mod(1:end/2))))
desired_ticks = [pi/4, pi/2, 3*pi/4, pi];
xticks(desired_ticks);
xticklabels({'\pi/4', '\pi/2', '3\pi/4', '\pi'});
xlabel('{\omega} (rads)')
ylabel('Arg{X(K)}')
title('Arg{X(K)} versus {\omega}')
xlim([0,pi])

% Restoring the signal
t_space = [0:1/Fs:size(x_t,1)/Fs-1/Fs].';
x_t_restored = sin((9000*(2*pi)).*t_space).*x_t_AM;
dft2(x_t_restored.',Fs);

% % play the result
% clip = audioplayer(x_t_restored, Fs);
% play(clip)
% pause(15)
% stop(clip)

% undo the amplitude scaling of the modulation process
x_t_restored_gain = x_t_restored*2;
% % play the result
% clip = audioplayer(x_t_restored_gain, Fs);
% play(clip)
% pause(15)
% stop(clip)

% -------------------------------------------------------------------------
% Question 7.4.4 - Hamming
% -------------------------------------------------------------------------

% Filter parameters to remove residual high-frequency component
f_c = 3000;
num_of_coeffs = 199;
TW = 3.44*Fs/num_of_coeffs;
f_1 = f_c+TW/2;
w_1 = f_1*2*pi/Fs;
n_space = [-(num_of_coeffs-1)/2:1:(num_of_coeffs-1)/2];
w_n_hamming = hamming(199).';
h1_n = w_1/pi*sinc(n_space*w_1/pi);

% produce the non-causal filter
h2_n = w_n_hamming.*h1_n;
t_space = [0:1/Fs:(size(h2_n,2)-1)/Fs];

figure(4);
subplot(1,2,2);
plot(t_space,h2_n)
title('Non-causal H_2(n)')
xlabel('Seconds (s)')
xlim([0 t_space(end)])
ylabel('|H_2(n)|')

h2_n = padarray(h2_n.',(num_of_coeffs-1)/2,0,'pre');
t_space = [0:1/Fs:(size(h2_n,1)-1)/Fs];
x_k = fft(h2_n.');
freq_res = Fs/size(h2_n,1);
adj_k_space = [0:freq_res:Fs/2];
x_k = x_k(1:size(adj_k_space,2));

figure(4);
subplot(1,2,1);
plot(t_space,h2_n)
title('Causal H_2(n)')
xlabel('Seconds (s)')
xlim([0 t_space(end)])
ylabel('|H_2(n)|')

fvtool(h2_n,1,'phase')

% Viewing the magnitude response of the designed FIR filter
dft2(h2_n.', Fs);

% Question 7.5
% Our impulse response is a bunch of scaled and time shifted deltas. Seeing
% as h2_n is causal, the elements within the h_2n are the coefficients of
% the numerator of the frequency response.
fvtool(h2_n,1,x_t_restored)

% Question 7.7 

% Compute the frequency response of the filter
[H, w] = freqz(h2_n, 1);

% Find the -3dB frequency programmatically
magdB = 20 * log10(abs(H));  % Convert magnitude to decibels
idx = find(magdB <= -3, 1, 'first');  % Find the first frequency point below -3dB
cutoff_frequency = w(idx) * (Fs / (2 * pi));  % Convert to Hz

% Find the stopband attenuation programmatically
idx = find(w*Fs/(2*pi) >= f_c+TW, 1, 'first');  % Find the first frequency point above 3000Hz
stopband_attenuation = magdB(idx);

% Question 7.8
% Filtering the restored signal using the filter
x_t_restored_filtered = conv(x_t_restored,h2_n,'same');
% undo the amplitude scaling of the modulation process
x_t_restored_filtered = x_t_restored_filtered*2;

% Viewing the results
dft2(x_t_restored_filtered.',Fs);

% play the result
clip = audioplayer(x_t_restored_filtered, Fs);
play(clip)
pause(15)
stop(clip)

fvtool(h2_n,1,x_t_restored_filtered)

% -------------------------------------------------------------------------
% Question 7.4.4 - Blackman
% -------------------------------------------------------------------------

% % Filter parameters to remove residual high-frequency component
% f_c = 3000;
% num_of_coeffs = 199;
% TW = 5.98*Fs/num_of_coeffs;
% f_1 = f_c+TW/2;
% w_1 = f_1*2*pi/Fs;
% n_space = [-(num_of_coeffs-1)/2:1:(num_of_coeffs-1)/2];
% blackman(num_of_coeffs);
% h1_n = w_1/pi*sinc(n_space*w_1/pi);
% 
% % produce the non-causal filter
% h2_n = w_n_blackman.*h1_n;
% x_k = dft2(h2_n.', Fs);
% close;
% freq_res = Fs/size(h2_n,2);
% adj_k_space = [0:freq_res:Fs/2];
% 
% figure(4);
% subplot(2,2,2);
% plot(n_space,h2_n)
% title('Non-causal H_2(n)')
% 
% subplot(2,2,4);
% plot(adj_k_space,unwrap(angle(x_k)))
% title('Phase response of non-causal H_2(n)')
% 
% h2_n = padarray(h2_n.',99,0,'pre');
% causal_n_space = horzcat(n_space,[(num_of_coeffs-1)/2+1:1:(num_of_coeffs-1)/2+99]);
% x_k = dft2(h2_n.', Fs);
% close
% freq_res = Fs/size(h2_n,2);
% adj_k_space = [0:freq_res:Fs/2];
% 
% figure(4);
% subplot(2,2,1);
% plot(causal_n_space,h2_n)
% title('Causal H_2(n)')
% 
% subplot(2,2,3);
% plot(adj_k_space,unwrap(angle(x_k)))
% title('Phase response of causal H_2(n)')
% 
% % Viewing the magnitude response of the designed FIR filter
% dft2(h2_n.', Fs);
% 
% % Question 7.5
% % Our impulse response is a bunch of scaled and time shifted deltas. Seeing
% % as h2_n is causal, the elements within the h_2n are the coefficients of
% % the numerator of the frequency response.
% fvtool(h2_n,1,x_t_restored)
% 
% % Question 7.7 
% % Filtering the restored signal using the filter
% x_t_restored_filtered = conv(x_t_restored,h2_n,'same');
% % undo the amplitude scaling of the modulation process
% x_t_restored_filtered = x_t_restored_filtered*2;
% 
% % Viewing the results
% dft2(x_t_restored_filtered.',Fs);
% 
% % play the result
% clip = audioplayer(x_t_restored_filtered, Fs);
% play(clip)
% pause(15)
% stop(clip)
% 
% % Question 7.8
% fvtool(h2_n,1,x_t_restored_filtered)
