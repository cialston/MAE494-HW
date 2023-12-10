
from scipy.optimize import minimize

# Objective function
def objective_function(x):
    x1, x2 = x
    return (x1 + 1)**2 + (x2 - 2)**2

# Constraint functions
def g1(x):
    return x[0] - 2

def g2(x):
    return x[1] - 1

def g3(x):
    return -x[0]

def g4(x):
    return -x[1]

# Initial guess
initial_guess = [0, 0]

# Constraints
constraints = [
    {'type': 'ineq', 'fun': g1},
    {'type': 'ineq', 'fun': g2},
    {'type': 'ineq', 'fun': g3},
    {'type': 'ineq', 'fun': g4},
]

# Minimize the objective function subject to constraints
result = minimize(objective_function, initial_guess, constraints=constraints)

# Extract optimal solution
optimal_solution = result.x

# Print the result
print("Optimal Solution:", optimal_solution)
print("Optimal Objective Value:", result.fun)