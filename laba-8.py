import matplotlib.pyplot as plt
import numpy as np

a = np.loadtxt(fname = 'grafik.txt', delimiter = ' ')

Y = []
X1 = []
X2 = []

for i in range(len(a)):
    for j in range(3):
        if j == 0:
            Y.append(a[i][j])
        elif j == 1:
            X1.append(a[i][j])
        else:
            X2.append(a[i][j])
            
plt.xlabel('rA')
plt.ylabel('V')
plt.plot(Y, X1, label = "Va")
plt.plot(Y, X2, label = "Vw")
plt.legend()
plt.show()
