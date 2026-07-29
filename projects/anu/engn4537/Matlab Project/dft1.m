function x_k=dft1(x_t,fs)

    % computing the DFT based on the number of samples in x_t
    x_k = zeros(1,fs);
    k_space = [0:fs-1];
    n_space = [0:size(x_t,2)-1];
    for k=k_space
        for n=n_space
            x_k(k+1) = x_k(k+1)+(x_t(n+1)*exp(-1i*2*pi/size(x_t,2)*n*k));
        end
    end
    x_k = x_k*2/size(x_t,2);

    % computing the magnitude
    x_k = abs(x_k);

    % computing the freq res
    freq_res = fs/size(x_t,2);
    % use freq res to create scaled k-space
    adj_k_space = [0:freq_res:fs/2];

    % get DFT magnitude values from 0 to Fs/2
    x_k = x_k(1:size(adj_k_space,2));
    
    % plot the result
    figure()
    stem(adj_k_space,x_k)
    xlim([0,fs/2])
    xlabel('K-space (Hz)')
    ylabel('|X(K)|')
    title('X(K) versus K')

end