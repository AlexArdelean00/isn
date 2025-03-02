import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("htopStats.csv")

t = range(1,601)

plt.figure()
plt.plot(t, data['CPU'])
plt.xlabel('tempo (s)')
plt.ylabel('CPU %')

plt.figure()
plt.plot(t, data['RAM'])
plt.xlabel('tempo (s)')
plt.ylabel('RAM %')

plt.show()