import numpy as np

z = np.random.random((10,2))
polar = np.zeros((10, 2))

for i in range(10):
    polar[i][0] = np.sqrt(z[i][0]**2 + z[i][1]**2)
    polar[i][1] = np.arctan2(z[i][1], z[i][0])

print(polar)