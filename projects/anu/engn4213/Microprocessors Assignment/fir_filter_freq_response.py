import numpy as np
import matplotlib.pyplot as plt

# FIR filter coefficients
coefficients = [-0.01238356,
  -0.1033217,
   0.81812371,
  -0.1033217,
  -0.01238356]

# Sampling frequency
sampling_frequency = 2000  # Hz

# Compute the frequency response of the FIR filter
frequency_response = np.abs(np.fft.fft(coefficients, 4096))
frequency_axis = np.fft.fftfreq(4096, 1 / sampling_frequency)

# Plot the frequency response
plt.figure()
plt.plot(frequency_axis[0:2048], 20 * np.log10(frequency_response)[0:2048])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain (dB)')
plt.title('Frequency Response of FIR Filter')
plt.grid(True)
plt.show()