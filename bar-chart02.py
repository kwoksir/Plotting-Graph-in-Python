# pip install matplotlib
# pip install numpy

import matplotlib.pyplot as plt
import numpy as np

data = ["Python", "C++", "Java", "JS", "C", "C#"]
ratings = [5.168, 5.726, 14.988, 3.165, 11.857, 4.453]
index = np.arange(len(data))

plt.bar(index, ratings)
plt.xticks(index, data)

plt.xlabel("X")
plt.ylabel("Usage")
plt.title("Programming Language Usage")
plt.savefig("graph.png")
plt.show()

