from scipy import random
import numpy as np
import matplotlib.pyplot as plt

a = 0
b = np.pi
N = 1000


def f(x):
    return np.sin(x)


areas = []

for i in range(N):
    xrand = np.zeros(N)
    for i in range(len(xrand)):
        xrand[i] = random.uniform(a, b)
    integral = 0.0

    for i in xrand:
        integral += f(i)
    ans = (b - a) / float(N) * integral
    areas.append(ans)


plt.title("Distributions of areas calculated")
plt.hist(areas, bins=30, ec="black")


plt.xlabel("Areas")
plt.show()
print(ans)
print(print(-np.cos(b) + np.cos(a)))
