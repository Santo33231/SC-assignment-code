




#a)We write a program to plot a line graph representing the temperature readings over a week: 20, 22, 19, 23, 21, 24, 20.
#Answer

import matplotlib.pyplot as plt

# Temperature data
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperatures = [20, 22, 19, 23, 21, 24, 20]

# Create plot
plt.figure(figsize=(8, 4))
plt.plot(days, temperatures, marker='o', color='red', linestyle='-')

# Add labels and title
plt.title('Weekly Temperature Readings')
plt.xlabel('Day of Week')
plt.ylabel('Temperature (°C)')
plt.grid(True)

# Show plot
plt.show()





#b) Write a program to generate the arithmetic sequence starting at 5 with a common difference of 3, for 8 terms

#Answer

# Arithmetic sequence parameters
start = 5
difference = 3
terms = 8

# Generate sequence
sequence = [start + i * difference for i in range(terms)]

print("Arithmetic sequence:", sequence)



#c)	Write a program to calculate the volume under the surface z = x^2 + y^2 over square region 0 < equal to x, y < equal to 1.
#Answer

import numpy as np
from scipy.integrate import dblquad

# Define the function z = x^2 + y^2
def func(y, x):
    return x**2 + y**2
	
# Define integration limits (0 to 1 for both x and y)
x_lower, x_upper = 0, 1
y_lower, y_upper = 0, 1

# Calculate the volume using double integration
volume, error = dblquad(func, x_lower, x_upper, lambda x: y_lower, lambda x: y_upper)

print(f"Volume under the surface: {volume:.4f}")
print(f"Estimated error: {error:.2e}")



