import matplotlib.pyplot as plt
import numpy as np

# El tipo de estilo que se utiliza
plt.style.use('_mpl-gallery-nogrid')

# crear datos: correlacionado + ruido
np.random.seed(1)
x = np.random.randn(5000)
y = 1.2 * x + np.random.randn(5000) / 3

# grafica:
fig, ax = plt.subplots()

ax.hexbin(x, y, gridsize=20)

ax.set(xlim=(-5, 5), ylim=(-5, 5))
ax.set_title("Gráfica hexágono")
plt.savefig("plot_hexbin")
plt.show()