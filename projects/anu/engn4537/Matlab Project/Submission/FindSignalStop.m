function [y,EndTime]=FindSignalStop(x_t)
    
    % Variable initialisation
    Fs = 48000;

    % Computing the spectrogram of the signal
    time_steps = 32; % Number of desired separate intervals of x_t
    WINDOW = size(x_t,1)./time_steps; % Corresponding window size
    NOVERLAP = 0; % Overlap between windows
    [S,F,T] = spectrogram(x_t,WINDOW,NOVERLAP,[],Fs);

    % Threshold all values in each signal power window less than 3,000 to 0
    thresholded = abs(S.^2)>3000;
    % Return the index of the first non-zero value of each row
    [~, first_indices] = max(thresholded, [], 1);
    % At this point, first_indices contains two clusterings (high freqs and
    % low freqs). We want to isolate the lower freqs.

    % binary threshold all the higher indices to be zero
    first_indices(first_indices>(max(first_indices)-min(first_indices))) = 0;
    % same as FindSignalStart but now we are interested in the LAST
    % non-zero window
    EndTime = T(find(fliplr(first_indices)~=0,1));
    % trim the input signal using the EndTime
    y = x_t(1:(EndTime*Fs),:);

end