import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq


def plot_dtft(x, n_points):
    # Compute the DTFT
    X = fft(x, n_points)
    freq = fftfreq(n_points, 1.0)  # Frequency axis

    # Plot the magnitude of the DTFT
    plt.plot(freq, np.abs(X))
    plt.title(f'Magnitude of {n_points}-point DFT')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.grid(True)


# Example sequence
n = int(input())  # adjust the length of the sequence as needed
x = np.array([1, 2, 3, 4])  # adjust the values of the sequence as needed

# Plot DTFT for different point DFTs
plt.subplot(2, 2, 1)
plot_dtft(x, 4)

plt.subplot(2, 2, 2)
plot_dtft(x, 8)

plt.subplot(2, 2, 3)
plot_dtft(x, 16)

plt.subplot(2, 2, 4)
plot_dtft(x, n)

plt.tight_layout()
plt.show()
