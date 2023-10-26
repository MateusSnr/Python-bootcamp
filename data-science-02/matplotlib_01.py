from matplotlib import pyplot as plt

"""
years = [2000, 2003, 1982, 1983, 1962, 1961]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7]

plt.plot(years, gdp, color='blue', marker='o',linestyle='solid')

plt.title("Nominal GDP")

plt.xlabel("Years")
plt.ylabel("Billions of R$")


plt.show()
"""

import math

x = [x * 0.1 for x in range(-100, 100)]

senx = [math.sin(xs) for xs in x]
cosx = [math.cos(xs) for xs in x]
tanx = [math.tan(xs) for xs in x]
arcsen = [math.sin(xs-1) for xs in x] # ? ou arcsen = [math.sin(xs)-1 for xs in x]

fig = plt.figure()
plt.plot(x, senx, 'r-', label="seno")
plt.plot(x, cosx, 'g--', label="cosseno")
#plt.plot(x, tanx, 'b-', label="tangente")
plt.plot(x, arcsen, 'b.', label="arco seno")

plt.legend(loc=2)
plt.show()



