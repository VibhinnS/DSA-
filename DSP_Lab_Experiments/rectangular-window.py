from __future__ import division
import numpy as np
from scipy import signal, fft
import matplotlib.pyplot as plt

wc = np.pi/4
M = 20
N = 512  # DFT size
n = np.arange(-M, M+1)  # corrected to include M+1 samples for symmetric range
h = wc/np.pi * np.sinc(wc*(n)/np.pi)  # see definition of np.sinc()

w, Hh = signal.freqz(h, 1, whole=True, worN=N)  # get entire frequency domain
wx = fft.fftfreq(len(w))  # shift to center for plotting

fig, axs = plt.subplots(3, 1)
fig.set_size_inches((8, 8))
plt.subplots_adjust(hspace=0.3)

ax = axs[0]
ax.stem(n, h, basefmt='b-')
ax.set_xlabel("n", fontsize=16)
ax.set_ylabel("amplitude", fontsize=16)

ax = axs[1]
ax.plot(w-np.pi, np.abs(fft.fftshift(Hh)))
ax.axis(xmax=np.pi/2, xmin=-np.pi/2)
ax.vlines([-wc, wc], 0, 1.2, color='g', lw=2., linestyle='--',)
ax.hlines(1, -np.pi, np.pi, color='g', lw=2., linestyle='--',)
ax.set_xlabel(r"w", fontsize=22)
ax.set_ylabel(r"H(w)", fontsize=22)
ax.grid()

ax = axs[2]
ax.plot(w-np.pi, 20*np.log10(np.abs(fft.fftshift(Hh))))
ax.axis(ymin=-40, xmax=np.pi/2, xmin=-np.pi/2)
ax.vlines([-wc, wc], 10, -40, color='g', lw=2., linestyle='--',)
ax.hlines(0, -np.pi, np.pi, color='g', lw=2., linestyle='--',)
ax.grid()
ax.set_xlabel(r"w", fontsize=22)
ax.set_ylabel(r"20log10 |H(w)|", fontsize=18)

plt.show()
