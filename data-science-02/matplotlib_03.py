from matplotlib import pyplot as plt
import math

"""
#Interface no estilo MATLAB

x = [x * 0.1 for x in range(-100, 100)]
senx = [math.sin(xs) for xs in x]
cosx = [math.cos(xs) for xs in x]

plt.figure()
plt.subplot(2, 2, 1)
plt.plot(x, senx)

plt.subplot(2, 1, 2)
plt.plot(x, cosx)

plt.show()
"""

#Interface orientada a objetos

x = [x * 0.1 for x in range(-100, 100)]
senx = [math.sin(xs) for xs in x]
cosx = [math.cos(xs) for xs in x]

fig, ax = plt.subplots(2)

ax[0].plot(x, senx)
ax[1].plot(x, cosx)

plt.show()

