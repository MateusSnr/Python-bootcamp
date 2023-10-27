from matplotlib import pyplot as plt
from IPython.display import Image
import math

x = [x * 0.1 for x in range(-100, 100)]
senx = [math.sin(xs) for xs in x]
cosx = [math.cos(xs) for xs in x]

fig = plt.figure()
plt.plot(x, senx, 'r-', label="seno")
plt.plot(x, cosx, 'b--', label="cosseno");
plt.legend(loc=2)
plt.show()

# Como salvar um gráfico como um arquivo PNG
fig.savefig('sin_and_cos_graphic.png')

# Exibindo o conteúdo do arquivo salvo
Image('sin_and_cos.png')

"""
Maneiras de colorir no matplotlib
    ° specify color by name - 'blue'
    ° short color code (rgbcmyk) - 'b'
    ° grayscale between 0 and 1 - '0.75'
    ° Hex code (RRGGBB from 00 to FF) - '#FFDD44')
    ° RGB tuple, values 0 to 1 - (1.0, 0.2, 0.3)
    ° all html color names supported - 'chartreuse'
    
"""

