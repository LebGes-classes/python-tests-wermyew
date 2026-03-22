[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Qb61TYzO)
# Python_tests
Задание на изучение тестирования в Python

# Задание
Файл: `math_utils.py`

Реализуй функции:

```python
def add(a, b):
    pass


def subtract(a, b):
    pass


def multiply(a, b):
    pass


def divide(a, b):
    pass
```

## ❗ Требования

- Поддержка `int` и `float`
- Если аргументы не числа → `TypeError`
- Деление на 0 → `ZeroDivisionError`

# Задача
- В качестве практической работы необходимо составить формализованное описание тестов.
- В качестве домашней работы необходимо реализовать тесты с помощью unittest и pytest по ранее созданному описанию тестов на языке Python и загрузить в свой репозиторий до крайнего срока.


# Тестирование в Python

## Что такое тестирование

**Тестирование** — это процесс проверки программы, чтобы убедиться, что она работает правильно, стабильно и предсказуемо.

Проще говоря:
> Ты написал код → тестирование отвечает на вопрос: *«А точно ли он делает то, что должен?»*

---

## Зачем нужно тестирование

- ✔ Уверенность, что код работает правильно
- ✔ Защита от поломок при изменениях
- ✔ Упрощение рефакторинга
- ✔ Документация поведения программы

---

## Пример

```python
def divide(a, b):
    return a / b
```

Без тестов:
- деление на 0 → ошибка
- некорректные типы → ошибка

С тестами:
- поведение заранее проверено
- ошибки обнаружены до пользователей

---

## Виды тестирования

- **Модульное (Unit testing)** — тестируем функции и классы
- **Интеграционное** — проверка взаимодействия частей системы
- **Системное** — тест всей системы

---

# Модульное тестирование

## Что это

Проверка отдельных частей программы:
- функций
- методов
- классов

## Цель

Проверить, что каждая часть работает корректно сама по себе.

---

## Принципы

1. **Изолированность**
2. **Повторяемость**
3. **Быстрота**
4. **Понятность**

---

## Структура теста (AAA)

- Arrange — подготовка
- Act — действие
- Assert — проверка

```python
def test_divide():
    a, b = 10, 2
    result = divide(a, b)
    assert result == 5
```

---

# unittest

Стандартная библиотека Python.

## Пример

```python
import unittest

def add(a, b):
    return a + b

class TestMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
```

## Основные методы

- `assertEqual(a, b)`
- `assertTrue(x)`
- `assertFalse(x)`
- `assertRaises(Exception, func, ...)`

---

## Пример проверки исключения

```python
def divide(a, b):
    return a / b

class TestDivide(unittest.TestCase):

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)
```

---

# pytest

Современная библиотека для тестирования.

## Преимущества

- меньше кода
- проще синтаксис
- мощные возможности

---

## Пример

```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
```

---

## Запуск

```bash
pytest
```

---

## Возможности

### Проверка исключений

```python
import pytest

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
```

---

### Параметризация

```python
import pytest

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (1, 1, 2),
    (0, 5, 5),
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```

---

### Fixtures

```python
import pytest

@pytest.fixture
def numbers():
    return 10, 5

def test_divide(numbers):
    a, b = numbers
    assert divide(a, b) == 2
```

---

# unittest vs pytest

| Критерий      | unittest | pytest |
|--------------|---------|--------|
| Синтаксис     | сложнее | проще |
| Структура     | классы  | функции |
| Расширяемость | ограничена | высокая |
| Популярность  | средняя | высокая |

---

# Когда писать тесты

- ✔ При написании кода (TDD)
- ✔ При исправлении багов
- ✔ Перед рефакторингом
