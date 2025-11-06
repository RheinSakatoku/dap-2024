## 1. Что такое динамическая типизация и чем она отличается от статической?

**Динамическая типизация** - это подход, когда типы переменных определяются во время выполнения программы.

**Статическая типизация** - типы переменных определяются на этапе компиляции.

### Основные различия:

| Характеристика | Динамическая типизация | Статическая типизация |
|----------------|------------------------|------------------------|
| Определение типа | Во время выполнения | Во время компиляции |
| Гибкость | Высокая | Ограниченная |
| Проверка ошибок | Во время выполнения | Во время компиляции |
| Примеры языков | Python, JavaScript | C++, Java, C# |

**Пример в Python (динамическая типизация):**
```python
x = 5        # x - int
x = "hello"  # x - str
x = [1,2,3]  # x - list
```

## 2. Чем отличается цикл for в Python от цикла for в С++?

### Python:
- Итерируется по элементам коллекции
- Автоматически управляет итератором
- Более высокоуровневый

```python
for element in collection:
    print(element)
```

### C++:
- Работает с индексами или итераторами
- Требует явного управления условием
- Более низкоуровневый

```cpp
for (int i = 0; i < size; i++) {
    cout << array[i] << endl;
}
```

## 3. Для чего предназначены операторы continue и break?

- **break** - полностью прерывает выполнение цикла
- **continue** - пропускает текущую итерацию и переходит к следующей

```python
for i in range(10):
    if i == 2:
        continue  # пропустит 2
    if i == 5:
        break     # остановится на 5
    print(i)
# Вывод: 0 1 3 4
```

## 4. Как определить функцию в python? Может ли функция возвращать несколько значений?

**Определение функции:**
```python
def function_name(parameters):
    """Docstring"""
    # тело функции
    return result
```

**Возврат нескольких значений** (фактически возвращается кортеж):
```python
def get_user_info():
    name = "Alice"
    age = 25
    return name, age

# Использование
user_name, user_age = get_user_info()
```

## 5. Что такое лямбда функции и для чего они предназначены?

**Лямбда-функции** - анонимные функции, определяемые в одной строке.

```python
# Обычная функция
def square(x):
    return x ** 2

# Лямбда-функция
square = lambda x: x ** 2
```

**Применение:**
```python
# Сортировка по ключу
users = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
sorted_users = sorted(users, key=lambda user: user['age'])

# Фильтрация
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
```

## 6. Может ли тело функции содержать определение другой функции?

**Да, может.** Это называется вложенной функцией.

```python
def outer_function(x):
    def inner_function(y):
        return y * 2
    return inner_function(x) + 10

result = outer_function(5)  # 20
```

## 7. Как определить класс в python? Для чего нужна переменная self?

**Определение класса:**
```python
class MyClass:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello, {self.name}"
```

**Переменная self** - ссылка на экземпляр класса, используется для доступа к атрибутам и методам объекта.

## 8. Как определить приватный метод? Можно ли вызвать приватный метод за пределами класса?

**Приватные методы** начинаются с двойного подчеркивания `__`.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # приватный атрибут
    
    def __validate_amount(self, amount):  # приватный метод
        return amount > 0
    
    def deposit(self, amount):
        if self.__validate_amount(amount):
            self.__balance += amount
```

**Технически можно вызвать**, но не рекомендуется:
```python
account = BankAccount(100)
account._BankAccount__validate_amount(50)  # так делать не стоит!
```

## 9. Как определить статический метод класса? Для чего может понадобиться статический метод?

**Статический метод** - метод, не требующий доступа к экземпляру класса.

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b

# Использование без создания экземпляра
result = MathUtils.add(5, 3)
```

**Применение:** утилитарные функции, не зависящие от состояния объекта.

## 10. Чем staticmethod отличается от classmethod?

| Аспект | @staticmethod | @classmethod |
|--------|---------------|--------------|
| Первый параметр | Нет специального | cls (класс) |
| Доступ к классу | Нет | Есть |
| Наследование | Не зависит | Зависит |

```python
class MyClass:
    class_attribute = "class value"
    
    @staticmethod
    def static_method():
        return "static method"
    
    @classmethod
    def class_method(cls):
        return f"class method: {cls.class_attribute}"
```

## 11. Как определить собственный класс исключений Python? Как выбросить и перехватить исключение?

**Создание пользовательского исключения:**
```python
class MyCustomError(Exception):
    def __init__(self, message, error_code):
        super().__init__(message)
        self.error_code = error_code
```

**Выброс и перехват исключения:**
```python
def validate_age(age):
    if age < 0:
        raise MyCustomError("Age cannot be negative", 1001)
    return age

try:
    validate_age(-5)
except MyCustomError as e:
    print(f"Error: {e}, Code: {e.error_code}")
except Exception as e:
    print(f"Other error: {e}")
```

## 12. Что такое кортеж, для чего он используется?

**Кортеж (tuple)** - неизменяемая упорядоченная коллекция элементов.

```python
# Создание кортежа
my_tuple = (1, 2, 3)
empty_tuple = ()
single_tuple = (1,)  # запятая обязательна!

# Без скобок (кортеж-пак)
packed = 1, 2, 3
```

**Преимущества и использование:**
- **Неизменяемость** - защита от случайных изменений
- **Производительность** - быстрее списков
- **Ключи словарей** - могут быть только хешируемые типы
- **Возврат нескольких значений** из функций

```python
# Использование как ключа словаря
coordinates = {(1, 2): "point A", (3, 4): "point B"}

# Распаковка
x, y, z = (1, 2, 3)

# Функции возвращают кортежи
def get_min_max(numbers):
    return min(numbers), max(numbers)

min_val, max_val = get_min_max([1, 5, 2, 8, 3])
```