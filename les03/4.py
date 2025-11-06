import numpy as np

z = np.random.rand(5, 10)
print(z)

for i in range(5):
    mid = 0
    for j in range(10):
        mid += z[i][j]
    mid = mid/10
    print(mid)
    for j in range(10):
        z[i][j] -= mid
    
print(z)