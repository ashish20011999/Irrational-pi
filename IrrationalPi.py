import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


fig, ax = plt.subplots(figsize=(5, 5))
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.set_facecolor('black')  


scatter = ax.scatter([], [], s=5, c='white', alpha=0.7)


def update(frame):
    theta = frame / 100.0  
    current_theta_values = np.linspace(0, theta, 1000)  
    complex_numbers = np.exp(1j * current_theta_values) + np.exp(np.pi * 1j * current_theta_values)
    real_part = np.real(complex_numbers)
    imag_part = np.imag(complex_numbers)
    scatter.set_offsets(np.column_stack((real_part, imag_part)))
    return scatter,


def animate_continuously(frame):
    while True:
        update(frame)
        yield frame
        frame += 1


ani = animation.FuncAnimation(fig, update, frames=animate_continuously(0), interval=10, blit=True)

plt.show()
