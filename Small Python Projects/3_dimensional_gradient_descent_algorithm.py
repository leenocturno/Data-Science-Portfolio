import numpy as np
import matplotlib.pyplot as plt

def function(x, y):
    return np.sin(5*x) * np.cos(5*y)/5 + 1

def calculate_gradient(x, y):
    return np.cos(5*x)*np.cos(5*y), -np.sin(5*x)*np.sin(5*y)

x=np.arange(-1, 1, 0.05)
y=np.arange(-1, 1, 0.05)

X, Y = np.meshgrid(x, y)
Z = function(X, Y)

current_pos = (0.8,0.4, function(0.7,0.4))
alpha = 0.03

converged = False
ax = plt.subplot(projection = '3d', computed_zorder = False)

for _ in range(1000):
    X_derivative, Y_derivative = calculate_gradient(current_pos[0], current_pos[1])
    X_new, Y_new = (current_pos[0] - alpha*X_derivative, current_pos[1]-alpha*Y_derivative)
    current_pos = (X_new, Y_new, function(X_new, Y_new))

    if (abs(X_derivative) < 1e-6 and abs(Y_derivative) < 1e-6 and not converged):
        print('Converged!')
        converged = True    

    ax.plot_surface(X, Y, Z, cmap='viridis', zorder = 0)
    ax.scatter(current_pos[0], current_pos[1], current_pos[2], color ='magenta', zorder = 1)

    if converged:
        ax.text(current_pos[0], current_pos[1], current_pos[2], 'Converged!', color = 'green', fontsize = 15, weight='bold')
        plt.pause(3)
        break

    plt.pause(0.01)
    ax.clear()

