import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the initial figure and axis
fig, ax = plt.subplots(figsize=(5, 5))
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.set_facecolor('black')  # Setting the background color to black

# Initialize an empty scatter plot with white color
scatter = ax.scatter([], [], s=5, c='white', alpha=0.7)

# Function to update the plot for each frame of the animation
def update(frame):
    theta = frame / 100.0  # Adjust the increment of theta as needed
    current_theta_values = np.linspace(0, theta, 1000)  # Generate theta values up to the current frame
    complex_numbers = np.exp(1j * current_theta_values) + np.exp(np.pi * 1j * current_theta_values)
    real_part = np.real(complex_numbers)
    imag_part = np.imag(complex_numbers)
    scatter.set_offsets(np.column_stack((real_part, imag_part)))
    return scatter,

# Create a function to run the animation continuously
def animate_continuously(frame):
    while True:
        update(frame)
        yield frame
        frame += 1

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=animate_continuously(0), interval=10, blit=True)

plt.show()
