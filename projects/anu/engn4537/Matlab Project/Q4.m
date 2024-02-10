close all
clear workspace

% Question 4.1

% load in the signals
x_1_t = audioread("Resource Files/DSP_Speech.wav");
x_2_t = load('Resource Files/DSP_HRIR/HRIR_1.mat');

% compute their fourier transforms using fft
N = size(x_1_t,1)+size(x_2_t,1)-1;
x_1_k = fft(x_1_t,N);
x_2_k = fft(x_2_t.HRIR_1,N);

% perform pointwise multiplication to get time-domain convolution result
y_k = x_1_k.*x_2_k;

% compute the inverse fourier transform using ifft
y_t_1 = ifft(y_k);

% plot the result
figure(1)
time = [0:1/16000:(size(x_1_t,1)-1)/16000];
stem(time,y_t_1)
xlabel('Time (seconds)')
ylabel('|y(t)|')
title('y(t) versus Time')

% verifying results
y_t_2 = conv(x_1_t,x_2_t.HRIR_1,'same');
time = [0:1/16000:(size(x_1_t,1)-1)/16000];
figure(2)
stem(time,y_t_2)
xlabel('Time (seconds)')
ylabel('|y(t)|')
title('y(t) versus Time')

% Question 4.2

% load in the signal
x_3_t = load('Resource Files/DSP_HRIR/HRIR_2.mat');

% perform the convolution
y_t_3 = conv(x_1_t,x_3_t.HRIR_2,'same');
time = [0:1/16000:(size(x_1_t,1)-1)/16000];

% view the result (delete later)
figure(3)
stem(time,y_t_3)
xlabel('Time (seconds)')
ylabel('|y(t)|')
title('y(t) versus Time')

% combine with the result from Q4.1
y_t = [y_t_2,y_t_3];

% save the resultant 2-channel vector as a .wav
audiowrite('Results/Binaural_Alder.wav',y_t,16000);

figure(4)
subplot(2,1,1)
time = [0:1/16000:(size(x_2_t.HRIR_1,1)-1)/16000];
stem(time,x_2_t.HRIR_1)
title('HRIR_1 versus Time')
ylabel('|HRIR_1|')
xlabel('Time (seconds)')
subplot(2,1,2)
time = [0:1/16000:(size(x_3_t.HRIR_2,1)-1)/16000];
stem(time,x_3_t.HRIR_2)
title('HRIR_2 versus Time')
ylabel('|HRIR_2|')
xlabel('Time (seconds)')