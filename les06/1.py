import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def load_dataset():
    #Загружает набор diabetes из sklearn и возвращает объект Bunch.
    diabetes = datasets.load_diabetes()
    return diabetes

def describe_dataset(diabetes):
    #Выводит описание набора данных и наименования признаков.
    print("=== Описание набора данных (DESCR) ===")
    print(diabetes.DESCR.split('\n')[0:15])  # печатаем начало описания, чтобы не засорять вывод
    print("... (полное описание доступно в diabetes.DESCR)\n")
    print("=== Имена признаков ===")
    print(list(diabetes.feature_names))
    print()

def create_dataframe(diabetes):
    #Создаёт DataFrame, содержащий признаки и целевое значение. Возвращает df.
    X = diabetes.data
    y = diabetes.target
    feature_names = diabetes.feature_names
    df = pd.DataFrame(X, columns=feature_names)
    df['target'] = y
    print("=== Первые 5 строк DataFrame ===")
    print(df.head())
    print()
    return df

def data_types_info(df):
    #Выводит информацию о типах данных, проверяет категориальные признаки и пропуски.
    print("=== Информация о типах данных ===")
    print(df.dtypes)
    print()
    # Категориальные признаки: в этом наборе — числовые признаки (не категориальные)
    # Проверим уникальные значения на случай дискретности
    nunique = df.nunique()
    categorical_like = nunique[nunique <= 10]  # грубая эвристика: <=10 уникальных значений
    print("=== Количество уникальных значений по столбцам ===")
    print(nunique)
    print()
    if categorical_like.empty:
        print("Нет явных категориальных признаков (по эвристике <=10 уникальных значений).")
    else:
        print("Признаки, похожие на категориальные (<=10 уникальных значений):")
        print(categorical_like)
    print()
    # Проверим пропуски
    print("=== Пропуски (null) по столбцам ===")
    print(df.isnull().sum())
    print()

def correlation_matrix(df, save_fig=False, fig_name='corr_matrix.png'):
    #Строит и возвращает матрицу корреляций (DataFrame). Также отображает heatmap (matplotlib).
    corr = df.corr()
    print("=== Матрица корреляций (фрагмент) ===")
    print(corr.round(3))
    print()
    # Визуализация
    plt.figure(figsize=(10,8))
    plt.title("Матрица корреляций (heatmap)")
    # простой heatmap без seaborn
    plt.imshow(corr, cmap='bwr', interpolation='none', aspect='auto')
    plt.colorbar()
    ticks = np.arange(len(corr.columns))
    plt.xticks(ticks, corr.columns, rotation=90)
    plt.yticks(ticks, corr.columns)
    plt.tight_layout()
    if save_fig:
        plt.savefig(fig_name, dpi=150)
        print(f"Heatmap сохранён в {fig_name}")
    plt.show()
    return corr

def plot_best_scatter(df, corr):
    #Находит признак с наибольшей по модулю корреляцией с target,строит scatter plot target vs этот признак и печатает коэффициент корреляции.
    target_corr = corr['target'].drop('target')
    best_feature = target_corr.abs().idxmax()
    best_value = target_corr.loc[best_feature]
    print(f"Признак с наибольшей корреляцией с target: '{best_feature}' (corr = {best_value:.3f})")
    plt.figure(figsize=(7,5))
    plt.scatter(df[best_feature], df['target'], alpha=0.7)
    plt.xlabel(best_feature)
    plt.ylabel('target')
    plt.title(f"Scatter: target vs {best_feature}\ncorr = {best_value:.3f}")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    return best_feature, best_value

def select_top_k_features(df, corr, k=5):
    #Формирует X из k признаков с наибольшей по модулю корреляцией с target. Возвращает X (DataFrame) и y (Series) и список выбранных признаков.
    target_corr = corr['target'].drop('target')
    topk = target_corr.abs().sort_values(ascending=False).head(k).index.tolist()
    print(f"Топ-{k} признаков по модулю корреляции с target: {topk}")
    X = df[topk].copy()
    y = df['target'].copy()
    print()
    return X, y, topk

def split_data(X, y, test_size=0.25, random_state=42):
    #Делит данные на train/test.
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    print(f"Размеры: X_train={X_train.shape}, X_test={X_test.shape}")
    print()
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    #Обучает простую линейную регрессию. Возвращает обученную модель.
    model = LinearRegression()
    model.fit(X_train, y_train)
    print("Модель LinearRegression обучена.")
    print("Коэффициенты модели:", model.coef_)
    print("Смещение (intercept):", model.intercept_)
    print()
    return model

def evaluate_model(model, X_test, y_test):
    #Вычисляет RMSE и R^2 для тестовой выборки и печатает их. Возвращает rmse, r2.
    y_pred = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    print(f"=== Оценка модели на тесте ===")
    print(f"RMSE = {rmse:.4f}")
    print(f"R^2  = {r2:.4f}")
    print()
    # график: реальные vs предсказанные
    plt.figure(figsize=(6,6))
    plt.scatter(y_test, y_pred, alpha=0.7)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], linestyle='--')
    plt.xlabel("y_реальные")
    plt.ylabel("y_предсказанные")
    plt.title("Реальные значения vs Предсказанные")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    return rmse, r2

def main():
    # 1. Загрузка
    diabetes = load_dataset()

    # 2. Описание и названия признаков
    describe_dataset(diabetes)

    # 3. Создание DataFrame (признаки + target)
    df = create_dataframe(diabetes)

    # 4. Информация о типах и пропусках
    data_types_info(df)

    # 5. Матрица корреляций
    corr = correlation_matrix(df)

    # 6. Scatter для признака с максимальной корреляцией
    best_feature, best_corr = plot_best_scatter(df, corr)

    # 7. Выбор топ-5 признаков по модулю корреляции
    X, y, top5 = select_top_k_features(df, corr, k=5)

    # 8. Разделение на train/test (test_size=0.25)
    X_train, X_test, y_train, y_test = split_data(X, y, test_size=0.25, random_state=42)

    # 9. Обучение модели
    model = train_model(X_train, y_train)

    # 10. Оценка модели: RMSE и R^2
    rmse, r2 = evaluate_model(model, X_test, y_test)

    # Возврат для дальнейшего использования, если понадобится
    return {
        'model': model,
        'top5_features': top5,
        'rmse': rmse,
        'r2': r2,
        'best_feature': best_feature,
        'best_feature_corr': best_corr
    }

if __name__ == "__main__":
    results = main()
