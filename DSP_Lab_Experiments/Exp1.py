import numpy as np
import matplotlib.pyplot as plt

# Define the range of values for the time variable
t = np.linspace(0, 5, 1000)

# Sinusoidal Function
sinusoidal_function = np.sin(2 * np.pi * t)
plt.subplot(3, 2, 1)
plt.plot(t, sinusoidal_function)
plt.title('Sinusoidal Function')
plt.grid(True)

# Unit Impulse Function
n = np.arange(-10, 11)  # Define the range of values for the discrete time variable 'n'
impulse_function = np.zeros_like(n)  # Initialize the impulse function with zeros
impulse_function[n == 0] = 1
plt.subplot(3,2,2)
plt.stem(n, impulse_function, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('Unit Impulse Function')
plt.grid(True)

# Unit Step Function
unit_step_function = np.heaviside(t, 1)
plt.subplot(3, 2, 3)
plt.plot(t, unit_step_function)
plt.title('Unit Step Function')
plt.grid(True)

# Unit Ramp Function
unit_ramp_function = np.maximum(0, t)
plt.subplot(3, 2, 4)
plt.plot(t, unit_ramp_function)
plt.title('Unit Ramp Function')
plt.grid(True)

# Exponential Function
exponential_function = np.exp(t)
plt.subplot(3, 2, 5)
plt.plot(t, exponential_function)
plt.title('Exponential Function')
plt.grid(True)

# Signum Function
signum_function = np.sign(t)
plt.subplot(3, 2, 6)
plt.plot(t, signum_function)
plt.title('Signum Function')
plt.grid(True)

# Adjust layout for better visibility
plt.tight_layout()

# Show the plot
plt.show()
