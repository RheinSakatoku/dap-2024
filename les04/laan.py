import pandas as pd
import numpy as np

def load_data(file_path):
    print("\n--- Задание 1: Загрузка данных ---")
    df = pd.read_csv(file_path, index_col="PassengerId")
    print("Данные загружены, индекс установлен на 'PassengerId'")
    return df

def head_data(df):
    print("\n--- Задание 2: Первые 6 строк ---")
    print(df.head(6))

def describe_data(df):
    print("\n--- Задание 3: Описание данных ---")
    print(df.describe(include='all'))

def gender_count(df):
    print("\n--- Задание 4: Сколько мужчин / женщин ---")
    print(df['Sex'].value_counts())

def pclass_distribution(df):
    print("\n--- Задание 4: Распределение Pclass ---")
    print("Общее распределение классов:")
    print(df['Pclass'].value_counts())
    print("\nРаспределение по полу:")
    print(df.groupby('Sex')['Pclass'].value_counts())
    male_2nd_class = df[(df['Sex']=='male') & (df['Pclass']==2)].shape[0]
    print("\nМужчин 2-го класса:", male_2nd_class)

def fare_stats(df):
    print("\n--- Задание 5: Медиана и стандартное отклонение Fare ---")
    median_fare = round(df['Fare'].median(), 2)
    std_fare = round(df['Fare'].std(), 2)
    print("Медиана Fare:", median_fare)
    print("Стандартное отклонение Fare:", std_fare)

def survival_by_age(df):
    print("\n--- Задание 6: Выживаемость по возрасту ---")
    young = df[df['Age'] < 30]
    old = df[df['Age'] > 60]
    young_surv = young['Survived'].mean()
    old_surv = old['Survived'].mean()
    print("Доля выживших <30:", round(young_surv, 2))
    print("Доля выживших >60:", round(old_surv, 2))

def survival_by_gender(df):
    print("\n--- Задание 7: Выживаемость женщин vs мужчин ---")
    male_surv = df[df['Sex']=='male']['Survived'].mean()
    female_surv = df[df['Sex']=='female']['Survived'].mean()
    print("Доля выживших мужчин:", round(male_surv, 2))
    print("Доля выживших женщин:", round(female_surv, 2))

def most_popular_male_name(df):
    print("\n--- Задание 8: Самое популярное мужское имя ---")
    male_names = df[df['Sex']=='male']['Name']
    first_names = male_names.apply(lambda x: x.split(',')[1].split('.')[1].strip())
    popular_name = first_names.value_counts().idxmax()
    print("Самое популярное мужское имя:", popular_name)

def avg_age_by_class_gender(df):
    print("\n--- Задание 10: Средний возраст по классу и полу ---")
    print(df.groupby(['Pclass','Sex'])['Age'].mean().round(2))

def avg_age_survived(df):
    print("\n--- Задание 10: Средний возраст выживших и погибших ---")
    print(df.groupby('Survived')['Age'].mean().round(2))
    print("\nВ среднем люди в 1 классе старше, чем во 2-ом, а те старше представителей 3-го класса")

# Вызовы функций
file_path = "data/titanic.csv"
df = load_data(file_path)

head_data(df)
describe_data(df)
gender_count(df)
pclass_distribution(df)
fare_stats(df)
survival_by_age(df)
survival_by_gender(df)
most_popular_male_name(df)
avg_age_by_class_gender(df)
avg_age_survived(df)
