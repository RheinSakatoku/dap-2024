import sys
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

def load_data(filename):
    #Извлечение данных из CSV 
    df = pd.read_csv(filename, index_col="PassengerId")
    print("Данные успешно загружены!")
    print("Первые 7 строк набора данных:\n")
    print(df.head(7))
    print()
    return df


def describe_data(df):
    #Информация о наборе данных 
    print("Информация о типах данных:")
    print(df.info())
    print()
    print("Проверка пропущенных значений:")
    print(df.isnull().sum())
    print()
    return df


def clean_data(df):
    #Удаление нечисловых и неинформативных признаков 
    df = df.drop(["Name", "Ticket", "Cabin"], axis=1)
    print("🧹 Удалены признаки: Name, Ticket, Cabin (не влияют напрямую на выживание)")
    print()
    return df


def encode_sex(df):
    #Кодирование пола 
    df["male"] = (df["Sex"] == "male").astype(int)
    df["female"] = (df["Sex"] == "female").astype(int)
    df = df.drop("Sex", axis=1)
    print("Признак 'Sex' заменён на 'male' и 'female'.")
    print()
    return df


def encode_embarked(df):
    #One-Hot кодирование порта посадки 
    df = pd.get_dummies(df, columns=["Embarked"], prefix="Embarked", dummy_na=False)
    print("Признак 'Embarked' закодирован (One-Hot Encoding).")
    print(f"Добавлены признаки: {', '.join([c for c in df.columns if 'Embarked_' in c])}")
    print()
    return df


def remove_nulls(df):
    #Удаление строк с пропущенными значениями 
    before = len(df)
    df = df.dropna()
    after = len(df)
    print(f"Удалено строк с пропусками: {before - after}")
    print()
    return df


def normalize_fare(df):
    #Нормализация признака 'Fare' 
    scaler = StandardScaler()
    df["Fare_norm"] = scaler.fit_transform(df[["Fare"]])
    print("⚖️ Признак 'Fare' нормализован (Fare_norm).")
    print()
    return df


def analyze_fare(df):
    #Разница средних значений 'Fare' между выжившими и погибшими 
    survived_mean = df[df["Survived"] == 1]["Fare"].mean()
    not_survived_mean = df[df["Survived"] == 0]["Fare"].mean()
    diff = survived_mean - not_survived_mean
    print(f"Разница средних значений 'Fare' (выжившие - погибшие): {diff:.2f}")
    print()
    return diff


def plot_fare_hist(df):
    #Гистограммы стоимости билета для выживших и погибших 
    plt.figure(figsize=(8, 5))
    plt.hist(df[df["Survived"] == 0]["Fare"], bins=30, alpha=0.6, label="Погибшие")
    plt.hist(df[df["Survived"] == 1]["Fare"], bins=30, alpha=0.6, label="Выжившие")
    plt.title("Распределение стоимости билета (Fare)")
    plt.xlabel("Fare")
    plt.ylabel("Количество пассажиров")
    plt.legend()
    plt.show()


def prepare_xy(df):
    #Формирование X и y
    y = df["Survived"]
    X = df.drop("Survived", axis=1)
    print("Наборы X и y сформированы.")
    print(f"Размер X: {X.shape}, размер y: {y.shape}")
    print()
    return X, y


def split_data(X, y):
    #Разделение на обучающую и тестовую выборки
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    print("Набор данных разделён (75% обучение, 25% тест).")
    print()
    return X_train, X_test, y_train, y_test


def train_model(X_train, y_train):
    #Обучение логистической регрессии
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    print("Модель логистической регрессии обучена.")
    print()
    return model


def evaluate_model(model, X_test, y_test):
    #Оценка точности и матрицы ошибок
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    acc = accuracy_score(y_test, y_pred)
    print("Матрица ошибок:")
    print(cm)
    print()
    print(f"Точность модели (accuracy): {acc:.4f}")
    print()
    return acc

def main():
    print(f"Python version: {sys.version}")
    print(f"Numpy version: {np.version.version}")
    print(f"Pandas version: {pd.__version__}")
    print(f"Matplotlib version: {mpl.__version__}")
    print()

    df = load_data("data/titanic.csv")
    describe_data(df)
    df = clean_data(df)
    df = encode_sex(df)
    df = encode_embarked(df)
    df = remove_nulls(df)
    df = normalize_fare(df)
    analyze_fare(df)
    plot_fare_hist(df)
    X, y = prepare_xy(df)
    X_train, X_test, y_train, y_test = split_data(X, y)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    main()

