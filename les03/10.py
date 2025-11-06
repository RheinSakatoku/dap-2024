import numpy as np

z = np.arange(100)
v = np.random.uniform(0,100)

index = np.argmin(np.abs(z - v))
closest = z[index]

print("Случайное число v:", v)
print("Ближайшее число в массиве:", closest)
