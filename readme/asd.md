- [**WEB PYTHON DEVELOPER**](#web-python-developer)
- [**BACKEND**](#backend)
  - [Ввод/вывод данных](#вводвывод-данных)
  - [Работа с переменными](#работа-с-переменными)
  - [Функции](#функции)
    - [Числовые](#числовые)
  - [Операторы](#операторы)
    - [Приоритет выполнения](#приоритет-выполнения)
    - [Математические](#математические)
    - [Для работы с последовательностями](#для-работы-с-последовательностями)
    - [Присваивания](#присваивания)
    - [Двоичные](#двоичные)
    - [Сравнения](#сравнения)
    - [Логические](#логические)
  - [Типы данных](#типы-данных)
    - [int/float](#intfloat)
      - [Математические функции math](#математические-функции-math)
      - [Форматирование чисел для вывода](#форматирование-чисел-для-вывода)
  - [Оператор ветвления if-else](#оператор-ветвления-if-else)
  - [Циклы](#циклы)
    - [for](#for)
    - [while](#while)
    - [Операторы break и continue](#операторы-break-и-continue)
    - [Функция range()](#функция-range)
  - [Модули](#модули)
    - [random](#random)
    - [time](#time)
    - [SymPy](#sympy)
    - [tkinter](#tkinter)
    - [math](#math)
    - [os](#os)
    - [Decimal](#decimal)
  - [Виртуальное окружение](#виртуальное-окружение)
  - [](#)
  - [Фреймворк Django](#фреймворк-django)
- [Многопоточность](#многопоточность)
- [ООП](#ооп)
  - [Методы](#методы)
- [Базы данных](#базы-данных)
  - [SQLAlchemy](#sqlalchemy)
    - [Типы данных](#типы-данных-1)
  - [Удаление данных, оператор DELETE](#удаление-данных-оператор-delete)
  - [Библиотека PyMySQL](#библиотека-pymysql)
  - [Библиотека dataclasses](#библиотека-dataclasses)
- [Переменные окружения](#переменные-окружения)
  - [Библиотека python-dotenv](#библиотека-python-dotenv)
- [**FRONTEND**](#frontend)

# **WEB PYTHON DEVELOPER**
# **BACKEND**
## Ввод/вывод данных

`print()` - для вывода данных используется функция.
```
print([<Объекты>] [, sep=' '][,end='\n'][,file=sys.stdout])
```
- Первый параметр — это набор объектов, которые нужно вывести.
- `sep=''` - между объектами автоматически вставляется разделитель — по умолчанию пробел.
- `end=''` - параметр end задает конец строки - по умолчанию используется символ '\п'.
- Последний параметр задает файл, в который осуществляется вывод.

`input()` - для ввода данных используется функция.
```
[<Переменная> = ] input ( [ <Сообщение>] )
```

## Работа с переменными

Переменные в Python представлены объектами. Точнее, для доступа к объекту используются переменные.
В самой переменной сохраняется ссылка на объект — адрес объекта в памяти.

- Имя (идентификатор) может начинаться с латинской буквы любого регистра, после которой можно использовать цифры. Пример правильных
имен переменных: ql, result 1, а, X, MyVar.
- Имя переменной не может начинаться с цифры. Пример неправильных
имен переменных: lq, 1 result.
- Имя переменной может начинаться с символа подчеркивания, но такие
имена имеют специальное значение для интерпретатора. Примеры таких
имен: resource,`__resource__`.
- Имя переменной не может быть ключевым словом.
- Лучше не переопределять встроенные идентификаторы.
- Имя переменной должно быть уникальным в пределах пространства
имен.

В Python также есть понятие:
- глобальной переменной
- локальные переменный считаются, объявленные внутри функции

## Функции
- `type()` - функция позволяет определить тип переменной
```
print(type([название_переменной]))
```
- `del` - используется для удаления переменной. Чтобы удалить несколько переменных, просто перечислите их в инструкции
del через запятую
```
z = 5
del z
a, b, c = 1, 2, 3
del a, b, c
```

### Числовые
- `аЬs(<число>)` - Возвращает абсолютное значение числа:
>Пример: abs(-5), abs(-7.5) = (5, 7.5)
- `bin(<число>)` - Преобразует десятичное число в двоичную систему, возвращает строку:
>Пример: bin(O), bin(333) = (' ObO ', ’0b01001101' )
- `divmod(a, b)` - Возвращает кортеж из двух значений — (а // b, а % Ь)
- `float(<число или строка>)` - Преобразует целое число или строку в вещественное число:
>Пример: float(3), float("2.2"), float("13.") = (3.0, 2.2, 13.0)
- `hех(<число>)`-  Преобразует десятичное число в шестнадцатеричную форму, возвращает строку
- `int(<объект> [, система счисления])` - Преобразует объект в целое число. Второй параметр позволяет указать систему счисления: 16 — шестнадцатеричная, 10 — десятичная (по умолчанию), 8 — восьмеричная, 2 — двоичная
>Пример: int(5.5), int("50", 10), int("0xfff", 16), int ("0o555", 8) = (5, 50, 4095, 365)
- `max(<список>)` `min(<список>)` - Возвращают максимальное/минимальное значение из заданного списка. Список задается через запятую:
>Пример: max(4, 7, 5), min(l, 4, 9) = (7, 1)
- `oct(<число>)` - Преобразует десятичное число в восьмеричную систему, возвращает строку
- `роw(<число>, <степень>[, К])` - Возводит указанное число в указанную степень. Последний параметр задает остаток от деления, то есть если он указан, то возвращается остаток от деления (число возводится в степень, делится на К и возвращается остаток).
>Например: pow(5, 2), pow(10, 2, 2), pow(10, 2, 3) = (25, 0, 1)
- `round(<число> [, N])` - Округляет число до ближайшего меньшего целого для чисел с дробной частью меньше 0.5 или до ближайшего большего целого для чисел с дробной частью больше 0.5. Если дробная часть равна 0.5, округление производится до ближайшего четного числа. Второй необязательный параметр N задает число знаков после точки.
>Пример: round (0.33), round (1.7), round(0.51) = (0, 2, 1)
- `sum(<последовательность>[,N])` - Возвращает сумму значений элементов последовательности плюс N (N — это начальное значение).
>Примеры: sum([1, 2, 3]), sum([1, 2, 3], 1) = (6, 7)

## Операторы
### Приоритет выполнения
1. `()` -	Скобки
2. `**` -	Возведение в степень
3. `+x`, `-x`, `~x` -	Унарные плюс, минус и битовое отрицание
4. `*`, `/`, `//`, `%` - Умножение, деление, целочисленное деление, остаток от деления
5. `+`, `-` -	Сложение и вычитание
6. `<<`, `>>` -	Битовые сдвиги
7. `&` - Битовое И
8. `^` - Битовое исключающее ИЛИ (XOR)
9. `|` - Битовое ИЛИ
10. `==`, `!=`, `>`, `>=`, `<`, `<=`, `is`, `is not`, `in`, `not in` - Сравнение, проверка идентичности, проверка вхождения
11. `not` -	Логическое НЕ
12. `and` -	Логическое И
13. `or` - Логическое ИЛИ

### Математические
- `+` - сложение
- `-` - вычитание
- `*` - умножение
- `/` - деление
- `//` - деление с остатком
- `%` - остаток от деления
- `**` - возведение в степень

### Для работы с последовательностями
- `+` - конкатенация
- `*` - повторение
- `in` - проверка на вхождение

### Присваивания
- `=` - присваивает переменной значение
- `+=` -  увеличивает значение переменной на указанную величину (или производит конкатенацию — для строк)
- `-=` - уменьшает значение переменной на указанную величину
- `*=` - умножает значение переменной на указанную величину (для строк этот оператор означает повтор)
- `/=` - делит значение переменной на указанную величину
- `//=` - то же, что и /=, но деление происходит с округлением вниз и присваиванием
- `%=` - деление по модулю и присваивание
- `**=` - возведение в степень и присваивание

### Двоичные
- `~` - двоичная инверсия (значение бита изменяется на противоположное: 1 на 0, 0 на 1)
- `&` — двоичное И
- `|` — двоичное ИЛИ
- `^` — двоичное исключающе ИЛИ
- `<<` — сдвиг влево (сдвигает двоичное представление числа влево на один или несколько разрядов, разряды справа заполняются нулями);
- `>>` — сдвиг вправо (сдвигает двоичное представление числа вправо на один или несколько разрядов, разряды слева заполняются нулями, если
число положительное, а если число отрицательное — единицами)

### Сравнения
- `=` — равно
- `!=` — не равно
- `<` — меньше
- `>` — больше
- `<=` — меньше или равно
- `>=` — больше или равно
- `in` — проверяет вхождение элемента в последовательность, возвращает True, если элемент встречается в последовательности
- `is` — проверяет, ссылаются ли две переменные на один и тот же объект. Если переменные ссылаются на один и тот же объект в памяти, оператор
возвращает True

### Логические
- `or` - логическое ИЛИ
- `and` - логическое И
- `not` - логическое отрицание

## Типы данных
- bool - Логический тип данных. Может содержать только два значения — true (истина) или false (ложь), что соответствует числам 1 и 0
- bytearray - Изменяемая последовательность байтов
- bytes - Неизменяемая последовательность байтов
- complex - Комплексные числа
- diсt - Словарь
- ellipsis - Используется для получения среза. Определяется или ключевым словом Ellipsis, или тремя точками
- frozenset - Неизменяемое множество
- function - Функция
- list - Список
- module - Модуль
- NoneType - Пустой объект, объект без значения (точнее со значением None, что в других языках соответствует null)
- set - Множество (набор уникальных объектов)
- str - Unicode-строка
- tuple - Кортеж
- type - Типы и классы данных
-
### int/float
- int - Целые числа. Размер числа ограничен только размером доступной оперативной памяти
- float - Вещественные числа

#### Математические функции math
```
import math
```
- `atan2(x, у)` - Аналогично atan(x/y). Если у равен 0, то возвращается pi/2
- `ceil(x)` - Возвращает наименьшее вещественное число с нулевой дробной частью — большее, чем число X
- `ехр(х)` - Возвращает е**х
- `fabs(x)` - Возвращает абсолютное значение числа х
- `floor(x)` - Наибольшее вещественное число с нулевой дробной частью — меньшее, чем число х
- `fmod(x, у)` - Возвращает остаток от деления х на у и эквивалентно х%у
- `hypot(x, у)` - Возвращает длину гипотенузы прямоугольника со сторонами длиной х и у и эквивалентно sqrt(x*x+y*y)
- `log(x)`, `loglO(x)` - Натуральный и десятичный логарифм числа х
- `modf(x)` - Возвращает кортеж из пары вещественных чисел - дробной и целой части х
- `sin(x)`, `cos(x)`, `tan(x)`, `asin(x)`, `acos(x)`, `atan(x)` - Всем известные стандартные и обратные тригонометрические функции (синус, косинус, тангенс, арксинус, арккосинус, арктангенс). Значение возвращается в радианах
- `sinh(x)`, `cosh(x)`, `tanh(x)` - Гиперболические синус, косинус, тангенс числа х
- `sqrt(x)` - Корень квадратный числа х



#### Форматирование чисел для вывода
Для форматирования одного числа для вывода используется встроенная функция `format()`. Например:
```
>>> х = 9876.54321
>>> # Два десятичных места точности
>>> format(х, '0.2f')
’9876.54'
>>> # Выравнивание по правому краю, 10 символов, 1 разряд точности
>>> format(х, '<10.1f')
'   9876.5'
>>> # Выравнивание по левому краю, 1 разряд
>>> format(х, '^10.1f')
'9876.5   '
>>> # Выравнивание по центру
>>> format(х, '^10.1f')
'   9876.5    '
>>> # Добавление разделителя тысяч
>>> format(х, ',')
'9,876.54321'
>>> format(х, '0,.1f')
'9,876.5'
```


Все типы данных в Python можно разделить на:
- неизменяемые - относятся числа, строки, кортежи и bytes
- изменяемые - относятся списки, словари и bytearray

## Оператор ветвления if-else
```
if <Логическое выражение>:
    <операторы, которые будут выполнены, если условие истинно>
elif <логическое выражение>:
    <операторы, которые будут выполнены, если условие истинно>
else:
    <операторы, которые будут выполнены, если условие ложно>
```

## Циклы
### for
```
for <элемент> in <последовательность>:
    <тело цикла>
else:
    <блок, который будет выполнен, если не Использовался оператор break>
```
Здесь элемент — это `<переменная>`, через которую будет доступен текущий элемент итерации.
`<Последовательность>` — объект, поддерживающий механизм итерации — строка, список, кортеж, словарь и т.д.
`<Тело цикла>` — операторы, которые будут выполняться при каждой итерации цикла.

Блок `else`, который, задает операторы, которые будут выполнены, если внутри цикла не использовался оператор break.
Данный блок не является обязательным, но вы можете его использовать.

### while
```
while <логическое выражением>:
    <тело цикла>
else:
    <блок, который будет выполнен, если не использовался оператор break>
```

### Операторы break и continue
- `break` - досрочно прерывает цикл
- `continue` - прерывает текущую итерацию и осуществляет переход на следующую

### Функция range()
Функция `range()` позволяет сгенерировать последовательность нужной длины.
```
range([начало,] конец [, шаг])
```













## Модули

### random
Модуль random - позволяет генерировать псевдослучайные числа.

`choice()` - возвращает случайный элемент из переданной ей последовательности, в роли которой может выступать строка, список, кортеж, или любая другая коллекция.

`randint(start, stop)` - возвращает случайное число (class 'int') в диапазоне от start до stop (обе границы включены в диапазон).

### time

Модуль time - модуль для работы со временем.

`time.sleep(сек)` - приостановить выполнение программы на заданное количество секунд.

### SymPy

SymPy — библиотека для символьных вычислений на языке Python.

Установите SymPy - `pip install sympy`

### tkinter

### math

`isprime()` - используется для определения, является ли заданное число простым числом или нет

`factorial` - возвращает факториал числа, т. е. произведение всех натуральных чисел от 1 до заданного числа.

### os

`os.getenv()` - возвращает значение ключа key переменной среды, если оно существует или значение по умолчанию default, если его нет. Значения key, default и возвращаемый результат - строки str.

### Decimal










## Виртуальное окружение
`D:` `C:` - команда терминала, для того чтобы перейти между дисками

`cd [путь]`- переход в нужый нам подкотолог

`python -m venv [имя виртуального окружения]` - создание виртуального окружения Python

`.\[имя виртуального окружения]\Scripts\activate` - запуск окружения

`deactivate` - чтобы выйти из виртуального окружения

##
`Фреймворк` - готовая модель программирования для быстрой разработки, на основе которой можно дописать собственный код.

## Фреймворк Django
`pip install django==[версия]` - установка django

`django-admin startproject [название проекта]` - создание проекта

Структура файлов проекта:
- >asgi.py -
- >settings.py -
  - >Структура файла setting.py
  - >INSTALLED_APPS - подключение приложений
- >urls.py -
- >wsgi.py -

`python manage.py runserver` - запуск проекта локально

`python manage.py startapp [название приложения]` - создание приложения

Структура файлов приложения:
- >admin.py - для настройки admin панели сайта
- >apps.py - для настройки конфигурирования текущего приложения
- >models.py - для хранения orm моделей для взаимодействия с базой данных
- >tests.py - модуль с тестирующими процедурами
- >views.py - для хранения представлений текущего приложения

Модель MTV(Model, Templates, Views) в Django













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

# Базы данных
## SQLAlchemy
[SQLAlchemy - от чайника к алхимику - руководство](https://massonnn.notion.site/SQLAlchemy-e2e50d4977374ed598e3b8b418258769)

Для создания моделей необходима базовая модель, от которой потом наследуются остальные модели. Начиная с версии SQLAlchemy 2.0 для создания базовой модели надо создать класс, унаследованный от DeclarativeBase.

Классы, которые наследуются от класса базовой модели, будут сопоставляться с таблицами в базе данных. Для сопоставления класса с определенной таблицей в БД применяется атрибут класса `__tablename__`. Например, определим модель Person

А так же для импортирования типов данных, нужно ипортировать Column(Колонка) и типы данных Integer, String и т.д.:

```
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import  Column, Integer, String

class Base(DeclarativeBase): pass

class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
```

### Типы данных
`String` - строка
`Integer` - целое число

- `unique` - уникальное значение
- `create_engine` - метод SQLAlchemy, который создает новый объект SQLAlchemy Engine , представляющий собой источник подключения к базе данных
- `Session` – непосредственно класс сессии. В его экземпляре хранятся изменения в текущей сессии, его можно настроить на автокоммит, он умеет отправлять данные в БД и ещё много чего.
- `query` -

## Удаление данных, оператор DELETE

Общая структура запроса с оператором DELETE
```
DELETE FROM имя_таблицы
[WHERE условие_отбора_записей];
```

## Библиотека PyMySQL

PyMySQL — позволяет устанавливать соединение с сервером MySQL для выполнения запросов и получения данных.

Установка PyMySQL - `pip3 install PyMySQL`

`connect(host='host', user='user', password='password', database='database', port='port', charset='charset')` - используется для установления соединения с базой данных MySQL.

## Библиотека dataclasses

`@dataclass` — предназначенное для создания классов, основное назначение которых — хранение данных.


# Переменные окружения
## Библиотека python-dotenv
Библиотека `python-dotenv` - позволяет загружать переменные окружения из файла .env в корневом каталоге приложения.

Установка python-dotenv - `pip install python-dotenv`

# **FRONTEND**