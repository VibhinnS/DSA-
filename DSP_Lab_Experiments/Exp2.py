import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve
# Function to perform circular convolution


def circular_convolution(signal1, signal2):
    return np.fft.ifft(np.fft.fft(signal1) * np.fft.fft(signal2))


# Define parameters for the sinusoidal signals
fs = 1000  # Sampling frequency
t = np.arange(0, 1, 1/fs)  # Time vector for 1 second
f1 = 5  # Frequency of the first sinusoidal signal
f2 = 10  # Frequency of the second sinusoidal signal

# Generate two sinusoidal signals
x1 = np.sin(2 * np.pi * f1 * t)
x2 = np.sin(2 * np.pi * f2 * t)

# Circular convolution of the sinusoidal signals
result_circular = circular_convolution(x1, x2)
result_linear = convolve(x1, x2, mode="full")
# Plot the original signals and the circular convolution result
plt.subplot(2, 2, 1)
plt.plot(t, x1)
plt.title('Sinusoidal Signal 1')
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(t, x2)
plt.title('Sinusoidal Signal 2')
plt.grid(True)

plt.subplot(2, 2, 3)
plt.plot(t, np.real(result_circular))  # Take real part since there might be small imaginary components
plt.title('Circular Convolution Result')
plt.grid(True)

plt.subplot(2, 2, 4)
plt.plot(t, result_linear[:len(t)], label='Linear Convolution', linestyle='dashed')
plt.title('Linear Convolution Result')
plt.grid(True)

plt.tight_layout()
plt.show()
