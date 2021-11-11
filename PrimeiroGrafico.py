import pandas
import matplotlib
import random
from matplotlib import pyplot as plt

dados1 = random.sample(range(100),k=20)
dados2 = random.sample(range(100),k=20)

plt.plot(dados1,dados2)
plt.show()
