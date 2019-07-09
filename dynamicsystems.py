# Important Notice: Everything that you might want to edit are in the lines 7 through 25

import math
import numpy as np
import matplotlib.pyplot as plt

# Initial value
x0 = 0

# Constant paramater
c = -1.99

# Range of both axis which the plot will be shown
x_range = 3
y_range = 3

# The function of the dynamic system
def func(x):
#   return ((2-x)/10)
#   return ((np.power(x, 4)) - (4 * (np.power(x, 2))) + 2)
#   return np.arctan(x)
#   return x**2
  return (np.power(x, 2) + c)
#   return -x*x*x + c
#   return abs(x-2)

x_points = []
x_points.append(x0)

iterations = 100

for i in range(1, iterations):
  point = func(x_points[i-1])
  x_points.append(point)

circuit_x = []
circuit_y = []

for j in range(0, len(x_points)):
  circuit_x.append(x_points[j])
  circuit_y.append(x_points[j])
  circuit_x.append(x_points[j])
  circuit_y.append(func(x_points[j]))
  
# print(x_points)
# print(circuit_x)
# print(circuit_y)

def identity(o): 
  return o

def axis_maker(x):
  return x*0

domain = np.arange(-x_range, x_range, 0.00001)

plt.figure(figsize=(15,15))
plt.axis([-x_range, x_range, -x_range, x_range])
plt.plot(circuit_x, circuit_y, 'k-')
plt.plot(circuit_x, circuit_y, 'ro')
plt.plot(domain, func(domain))
plt.plot(domain, identity(domain))
plt.plot(domain, axis_maker(domain), 'k')
plt.plot(axis_maker(domain), domain, 'k')
plt.show()

