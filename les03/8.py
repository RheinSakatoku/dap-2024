import numpy as np

z = np.ones(10)
i = np.random.randint(0,len(z),20)
print(i)

i = np.unique(i)
print(i)

z[i] += 1

print(z)