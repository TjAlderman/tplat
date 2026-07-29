close all
clear workspace

% Question 3.1
t = [0:(1/4800):((7200-1)/4800)];
x_t = 1.2*cos(2*pi*150*t)+2*sin(2*pi*728*t);

figure(1)
stem(t,x_t)
xlabel('Time (seconds)')
ylabel('|x(t)|')
title('x(t) versus Time')

figure(2)
plot(t,x_t)
xlabel('Time (seconds)')
ylabel('|x(t)|')
title('x(t) versus Time')

% Question 3.2

% computing the DFT
x_k = dft1(x_t,4800);
% adjusting plot parameters
ylim([0,2.2])

% Question 3.3

% computing the DFT
x_k = dft2(x_t,4800);
% adjusting plot parameters
ylim([0,2.2])

% Question 3.4

% DFT1
minTime=inf; REPS=5;
tic; % start a timer for average time
for i=1:REPS
    tstart = tic; % start a timer for mintime
    dft1(x_t,4800);
    telapsed = toc(tstart); % record the duration of the function
    close % close the plot opened by dft1
    minTime = min(telapsed,minTime); % save the time if it was the minimum of previous runs
end
averageTime = toc/REPS; % compute the average time

fprintf('\nThe average time for dft1 is: %f', averageTime);
fprintf('\nThe minimum time for dft1 is: %f', minTime);

% DFT2
minTime=inf; REPS=5;
tic; % start a timer for average time
for i=1:REPS
    tstart = tic; % start a timer for mintime
    dft2(x_t,4800);
    telapsed = toc(tstart); % record the duration of the function
    close % close the plot opened by dft2
    minTime = min(telapsed,minTime); % save the time if it was the minimum of previous runs
end
averageTime = toc/REPS; % compute the average time

fprintf('\nThe average time for dft2 is: %f', averageTime);
fprintf('\nThe minimum time for dft2 is: %f', minTime);

% Question 3.5

% computing the DFT
x_k = dft2(x_t,4800);

% adjusting plot parameters
xlim([0,4800/2])
ylim([0,2.2])


% Question 3.6

% CASE 1
% computing the DFT
x_k = dft2(x_t(1:32),4800);
% adjusting plot parameters
xlim([0,4800/2])
ylim([0,2.2])
title('Case 1: X(K) versus K')

% CASE 2
% computing the DFT
padded_x_t = x_t(1:32);
padded_x_t = padarray(padded_x_t,[0,(512-32)/2],0,'both');
x_k = dft2(padded_x_t,4800);
% adjusting plot parameters
xlim([0,4800/2])
ylim([0,0.13])
title('Case 2: X(K) versus K')

% CASE 3
% computing the DFT
x_k = dft2(x_t(1:512),4800);
% adjusting plot parameters
xlim([0,4800/2])
ylim([0,2.2])
title('Case 3: X(K) versus K')
