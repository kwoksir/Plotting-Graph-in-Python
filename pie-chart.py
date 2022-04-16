# pip install matplotlib
import matplotlib.pyplot as plt

country = ["China", "Japan", "USA", "UK"]
data = [100,80,70,50]
colorList = ["red", "green", "blue", "yellow"]

exp = (0,0,0.05,0)
plt.pie(data, explode=exp, labels = country, colors = colorList, labeldistance = 1.1, autopct = "%3.1f%%", shadow = True, startangle = 90, pctdistance = 0.6)
plt.axis("equal")
plt.legend()
plt.title("Country power")
plt.show()
