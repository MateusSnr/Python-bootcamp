"""
import sympy as sp
import numpy as np
import cmath
from matplotlib import pyplot as plt
from sympy import(asin, acos, atan)

years = [2000, 2003, 1982, 1983, 1962, 1961]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7]

plt.plot(years, gdp, color='blue', marker='o',linestyle='solid')

plt.title("Nominal GDP")

plt.xlabel("Years")
plt.ylabel("Billions of R$")


plt.show()

----------------------------------------------------------

import math

x = [x * 0.1 for x in range(-100, 100)]

senx = [math.sin(xs) for xs in x]
cosx = [math.cos(xs) for xs in x]
tanx = [math.tan(xs) for xs in x]
asin_values = [np.real(sp.asin(xs)) for xs in x] # ? ou arcsen = [math.sin(xs)-1 for xs in x]
print(asin)

fig = plt.figure()
plt.plot(x, senx, 'r-', label="seno")
plt.plot(x, cosx, 'g--', label="cosseno")
#plt.plot(x, tanx, 'b-', label="tangente")
plt.plot(x, asin, 'b.', label="arco seno")

plt.legend(loc=2)
plt.show()
------------------------------------------------------
"""
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import math

x = [x * 0.1 for x in range(-100, 101)]

senx = [math.sin(xs) for xs in x]
cosx = [math.cos(xs) for xs in x]
asin_values = []

for xs in x:
    # Check if xs is within the valid range [-1, 1]
    if -1 <= xs <= 1:
        # Calculate inverse sine only for valid input values
        asin_values.append(np.real(sp.asin(xs)))
    else:
        # Handle values outside the valid range (you can skip or handle them as needed)
        asin_values.append(None)  # Placeholder for invalid values

fig = plt.figure()
plt.plot(x, senx, 'r-', label="Sine")
plt.plot(x, cosx, 'g--', label="Cosine")
plt.plot(x, asin_values, 'b.', label="Inverse Sine")

plt.legend(loc=2)
plt.xlabel('x')
plt.ylabel('Value')
plt.title('Trigonometric Functions')
plt.grid(True)
plt.show()







