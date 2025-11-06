import numpy as np

matrix = [[(i+j) % 2 for j in range(8)] for i in range(8)]

for row in matrix:
    print(row)
