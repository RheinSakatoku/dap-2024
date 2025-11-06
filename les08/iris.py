import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN

# ----------------------
# 1. Загружаем данные
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)

# ----------------------
# 2. Нормализация данных
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ----------------------
# 3. Кластеризация DBSCAN
# Подбирай eps и min_samples для лучшего результата
dbscan = DBSCAN(eps=0.5, min_samples=5)
clusters = dbscan.fit_predict(X_scaled)

# ----------------------
# 4. Диаграмма рассеяния
plt.figure(figsize=(8,6))
plt.scatter(
    X_scaled[:, 0],  # sepal length
    X_scaled[:, 1],  # sepal width
    c=clusters,      # цвет по кластерам
    cmap='rainbow',
    s=50
)
plt.xlabel('Sepal Length (scaled)')
plt.ylabel('Sepal Width (scaled)')
plt.title('DBSCAN Clustering of Iris Dataset')
plt.show()

# ----------------------
# 5. Вывод
print("Уникальные кластеры, найденные DBSCAN:", np.unique(clusters))
print("Кластеры: -1 обозначает шум (точки, не вошедшие ни в один кластер)")
