**PYTHON DEVELOPER**


- [Модули](#модули)
  - [random](#random)
  - [time](#time)
  - [SymPy](#sympy)
  - [math](#math)
- [Многопоточность](#многопоточность)
- [ООП](#ооп)
  - [Методы](#методы)

# Модули

## random
Модуль random - позволяет генерировать псевдослучайные числа.

`choice()` - возвращает случайный элемент из переданной ей последовательности, в роли которой может выступать строка, список, кортеж, или любая другая коллекция.

`randint(start, stop)` - возвращает случайное число (class 'int') в диапазоне от start до stop (обе границы включены в диапазон).

## time

Модуль time - модуль для работы со временем.

`time.sleep(сек)` - приостановить выполнение программы на заданное количество секунд.

## SymPy

SymPy — библиотека для символьных вычислений на языке Python.

Установите SymPy - pip install sympy

## math

`isprime()` - используется для определения, является ли заданное число простым числом или нет

`factorial` - возвращает факториал числа, т. е. произведение всех натуральных чисел от 1 до заданного числа.

# Многопоточность

`import threading` - модуль предоставляет удобные средства для работы с потоками.

**Пример:**
```
import threading

def print_numbers():
    for i in range(5):
        print(i)

# Создаем поток
thread = threading.Thread(target=print_numbers)

# Запускаем поток
thread.start()

# Ожидаем завершения потока
thread.join()

print("Главный поток завершен")
```

# ООП
## Методы

`__init__()` - метод-конструктор, который вызывается автоматически при создании нового экземпляра класса. Он используется для инициализации атрибутов объекта. То есть, это метод, в котором можно задать начальные значения для переменных объекта (экземпляра класса).

`__str__()` - используется для определения строкового представления объекта. Когда объект передается в функцию `print()` или преобразуется в строку с помощью `str()`, вызывается именно метод `__str__()`. Этот метод возвращает строку, которая будет выводиться пользователю.
