import numpy as np

z = np.arange(11)
for i in range(len(z)):
    if z[i] > 3 and z[i] < 8:
        z[i] = z[i]* -1
    
print(z)