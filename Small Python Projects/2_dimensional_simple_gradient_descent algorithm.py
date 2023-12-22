import numpy as np
import matplotlib.pyplot as plt

def function(x):
    return x**2

def y_derivative(x):
    return 2*x

x = np.arange(-100, 100, 0.1)
y = function(x)

current_pos = (90, function(x))
alpha = 0.09

converged = False 

for _ in range(1000):
    new_x = current_pos[0] - alpha * y_derivative(current_pos[0])
    new_y = function(new_x)
    current_pos = (new_x, new_y)

    if abs(y_derivative(current_pos[0])) < 1e-6 and not converged:
        converged = True

    plt.plot(x, y, color = 'gray')
    plt.scatter(current_pos[0], current_pos[1], color='magenta')
    
    if converged:
        plt.text(current_pos[0], current_pos[1], 'Converged!', color = 'green', fontsize = 12)
        plt.pause(3)
        break

    plt.pause(0.001)
    plt.clf()

