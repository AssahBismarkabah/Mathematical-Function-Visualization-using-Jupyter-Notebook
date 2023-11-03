import numpy as np
import matplotlib.pyplot as plt

# Define a function to plot a sine wave
def plot_sine_wave(x):
  y = np.sin(x)
  plt.plot(x, y)

# Call the function to plot a sine wave
plot_sine_wave(np.linspace(0, 2*np.pi, 100))

# Display the plot
plt.show()
