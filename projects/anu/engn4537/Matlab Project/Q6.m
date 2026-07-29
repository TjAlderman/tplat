% Question 6.1
x = audioread("Results/DSP_TimothyAlder.wav");
fvtool(x,1)

fvtool([0.9504,-1.8484,0.9504],[1,-1.8484,0.9009])

fvtool([0.0945,-0.129,0.0945],[1,-1.6244,0.6832])

fvtool([0.2346,-0.3187,0.2346],[1,0.4419,0.2231])

% Question 6.2

x = audioread("Results/DSP_TimothyAlder.wav");
y = filter([0.0945,-0.129,0.0945],[1,-1.6244,0.6832],x);
fvtool([0.0945,-0.129,0.0945],[1,-1.6244,0.6832],y);
audiowrite('Results/DSP_H2_Filtered_TimothyAlder.wav',y,48000);

% Question 6.3

x = audioread("Results/DSP_TimothyAlder.wav");
y = filter([1,-1.93,1],[1,-1.91,0.98],x);
fvtool([1,-1.93,1],[1,-1.91,0.98],y)
audiowrite('Results/DSP_H4_Filtered_TimothyAlder.wav',y,48000);
fvtool([1,-1.93,1],[1,-1.91,0.98],'polezero');