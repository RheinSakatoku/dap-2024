import numpy as np

z = np.random.random(10)
z[z == np.max(z)] = 0

print(z)