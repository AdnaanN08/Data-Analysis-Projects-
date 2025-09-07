import numpy as np
import random
from mean_var_std import calculate

# Generate a random list of 9 digits (0-9)
random_list = [random.randint(0, 9) for _ in range(9)]


print("Random 9-digit list:", random_list)
print("3x3 Matrix:")
matrix = np.array(random_list).reshape(3, 3)
print(matrix)
print()

# Calculate statistics
result = calculate(random_list)

print("Results:")
print("{")
for i, (stat_name, values) in enumerate(result.items()):
    comma = "," if i < len(result) - 1 else ""
    print(f"  '{stat_name}': [axis1={values[0]}, axis2={values[1]}, flattened={values[2]}]{comma}")
print("}")