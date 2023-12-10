import numpy as np
import matplotlib.pyplot as plt

# Objective function
def objective_function(x1, x2):
    return (x1 + 1)**2 + (x2 - 2)**2

# Constraint functions
def g1(x1):
    return x1 - 2

def g2(x2):
    return x2 - 1

def g3(x1):
    return -x1

def g4(x2):
    return -x2

# Create a meshgrid for x1 and x2
x1 = np.linspace(-3, 3, 100)
x2 = np.linspace(-3, 3, 100)
X1, X2 = np.meshgrid(x1, x2)

# Evaluate objective and constraint functions on the meshgrid
Z = objective_function(X1, X2)
G1 = g1(x1)
G2 = g2(x2)
G3 = g3(x1)
G4 = g4(x2)

# Plot objective function
plt.contour(X1, X2, Z, levels=20, cmap='viridis', label='Objective Function')

# Plot constraint functions
plt.plot(x1, G1, label=r'$g_1(x_1) = x_1 - 2 \leq 0$')
plt.axhline(y=1, color='r', linestyle='--', label=r'$g_2(x_2) = x_2 - 1 \leq 0$')
plt.plot(x1, G3, label=r'$g_3(x_1) = -x_1 \leq 0$', linestyle='dashed')
plt.axhline(y=-2, color='orange', linestyle='dotted', label=r'$g_4(x_2) = -x_2 \leq 0$')

# Add labels and legend
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.title('Problem 1')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()


