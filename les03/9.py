import numpy as np

z = np.array([1,2,3,4,5])
arr = []

for i in range(len(z)):
    arr.append(int(z[i]))
    if i+1 != len(z):
        arr.append(0)
        arr.append(0)
        arr.append(0)

print(arr)