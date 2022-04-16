# pip install matplotlib
import matplotlib.pyplot as plt

listx1 = [1,5,7,9,13,16]
listy1 = [15,50,80,40,70,50]

listx2 = [2,6,8,11,14,16]
listy2 = [10,40,30,50,80,60]

plt.bar(listx1, listy1, label="Boy")
plt.bar(listx2, listy2, label="Girl", color="red", linestyle="--")
plt.legend()
plt.xlim(0,20)
plt.ylim(0,100)
plt.xlabel("Age")
plt.ylabel("Pocket Money")
plt.title("Pocket Money (Boy vs Girl)")

plt.show()
