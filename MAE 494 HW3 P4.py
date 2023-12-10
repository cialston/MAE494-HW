from scipy.optimize import minimize

# Define the objective function and constraints
def objective(x):
    return x[0]**2 + x[1]**2 + x[2]**2

def constraint1(x):
    return (x[0]**2)/4 + (x[1]**2)/5 + (x[2]**2)/25 - 1

def constraint2(x):
    return x[0] + x[1] - x[2]

# Initial guess
initial_guess = [1, 1, 1]

# Define constraints as dictionary
constraints = (
    {'type': 'eq', 'fun': constraint1},
    {'type': 'eq', 'fun': constraint2}
)

# Solve the optimization problem
result = minimize(objective, initial_guess, constraints=constraints)

# Print the result
print(result)
