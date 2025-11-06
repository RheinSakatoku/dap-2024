import numpy as np

# создаём массив 10x10 со случайными числами от 1 до 100
matrix = np.random.randint(1, 101, size=(10, 10))
print("Массив:\n", matrix)

# находим минимум и максимум
min_val = matrix.min()
max_val = matrix.max()

print("Минимум:", min_val)
print("Максимум:", max_val)
