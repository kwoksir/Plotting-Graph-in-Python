# pip install matplotlib
# pip install numpy

import matplotlib.pyplot as plt
import numpy as np

start = 0
stop = 10
num = 100

x = np.linspace(start,stop,num)
sin = np.sin(x)
cos = np.cos(x)

plt.plot(x, sin, "r-o", label="sin(x)")
plt.plot(x, cos, "g--", label="cos(x)")

plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Sine and Cosine Curve")
plt.savefig("graph.png")
plt.show()

