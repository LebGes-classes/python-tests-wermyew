import unittest
import pytest


def add(a, b):
    # проверка типов аргументов
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):

        raise TypeError("аргументы должны быть числами (int или float)")

    return a + b


def subtract(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):

        raise TypeError("аргументы должны быть числами (int или float)")

    return a - b


def multiply(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):

        raise TypeError("аргументы должны быть числами (int или float)")

    return a * b


def divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):

        raise TypeError("аргументы должны быть числами (int или float)")

    # проверка деления на ноль
    if b == 0:

        raise ZeroDivisionError("нельзя делить на ноль")

    return a / b


class TestMath(unittest.TestCase):
    """Класс для тестирования математических операций с использованием unittest"""

    # тестирование сложения
    @pytest.mark.feature('add')
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(100, 200), 300)
        self.assertEqual(add(-2, -5), -7)
        self.assertAlmostEqual(add(2.5, 3.6), 6.1)
        self.assertEqual(add(2, 0), 2)

    # тестирование вычитания
    @pytest.mark.feature('subtract')
    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(5, 8), -3)
        self.assertEqual(subtract(6, 0), 6)
        self.assertEqual(subtract(-3, -3), 0)
        self.assertAlmostEqual(subtract(4.6, 1.4), 3.2)

    # тестирование умножения
    @pytest.mark.feature('multiply')
    def test_multiply(self):
        self.assertEqual(multiply(3, 0), 0)
        self.assertEqual(multiply(3, 5), 15)
        self.assertEqual(multiply(-3, -1), 3)
        self.assertEqual(multiply(-13, 2), -26)
        self.assertAlmostEqual(multiply(-1.6, -2.5), 4.0)

    # проверка выброса исключения при делении на ноль
    @pytest.mark.feature('divide')
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    # тестирование нескольких случаев деления
    @pytest.mark.feature('divide')
    def test_divide(self):
        test_cases = [
            (10, 2, 5),
            (-10, 2, -5),
            (0, 5, 0),
        ]

        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(divide(a, b), expected)

        # тестирование деления с float
        self.assertAlmostEqual(divide(4.5, 2.5), 1.8)

    # проверка TypeError при неверных типах для add
    @pytest.mark.feature('add')
    def test_add_type_error(self):
        with self.assertRaises(TypeError):
            add("2", 3)

        with self.assertRaises(TypeError):
            add(2, "3")

        with self.assertRaises(TypeError):
            add("2", "3")

        with self.assertRaises(TypeError):
            add(None, 3)

        with self.assertRaises(TypeError):
            add([1, 2], 3)

    # проверка TypeError при неверных типах для subtract
    @pytest.mark.feature('subtract')
    def test_subtract_type_error(self):
        with self.assertRaises(TypeError):
            subtract("5", 2)

        with self.assertRaises(TypeError):
            subtract(5, "2")

    # проверка TypeError при неверных типах для multiply
    @pytest.mark.feature('multiply')
    def test_multiply_type_error(self):
        with self.assertRaises(TypeError):
            multiply("3", 5)

        with self.assertRaises(TypeError):
            multiply(3, "5")

    # проверка TypeError при неверных типах для divide
    @pytest.mark.feature('divide')
    def test_divide_type_error(self):
        with self.assertRaises(TypeError):
            divide("10", 2)

        with self.assertRaises(TypeError):
            divide(10, "2")


if __name__ == "__main__":
    unittest.main()


# тесты с помощью pytest
# параметризация
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (100, 200, 300),
    (-2, -5, -7),
    (0, 5, 5),
    (2.5, 3.6, 6.1),
])


# параметризованный тест для add
@pytest.mark.feature('add')
def test_add_parametrized(a, b, expected):
    if isinstance(expected, float):
        assert add(a, b) == pytest.approx(expected)
    else:
        assert add(a, b) == expected


# тестирование вычитания
@pytest.mark.feature('subtract')
def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(5, 8) == -3
    assert subtract(6, 0) == 6
    assert subtract(-3, -3) == 0
    assert subtract(4.6, 1.4) == pytest.approx(3.2)


# тестовые данные для умножения
@pytest.fixture
def multiply_data():

    return [
        (-2, 3, -6),
        (5.2, 2, 10.4),
        (3, 4, 12),
        (10, 0, 0),
    ]


# тестирование multiply с фикстурой
@pytest.mark.feature('multiply')
def test_multiply_with_fixture(multiply_data):
    for a, b, expected in multiply_data:
        if isinstance(expected, float):
            assert multiply(a, b) == pytest.approx(expected)
        else:
            assert multiply(a, b) == expected


# проверка выброса исключения при делении на ноль
@pytest.mark.feature('divide')
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError, match="нельзя делить на ноль"):
        divide(10, 0)


# тестирование деления
@pytest.mark.feature('divide')
def test_divide():
    assert divide(10, 2) == 5
    assert divide(-10, 2) == -5
    assert divide(0, 5) == 0
    assert divide(4.5, 2.5) == pytest.approx(1.8)


# проверка TypeError при неверных типах для add
@pytest.mark.feature('add')
def test_add_type_error():
    with pytest.raises(TypeError, match="аргументы должны быть числами"):
        add("2", 3)

    with pytest.raises(TypeError):
        add(2, "3")

    with pytest.raises(TypeError):
        add("2", "3")

    with pytest.raises(TypeError):
        add(None, 3)

    with pytest.raises(TypeError):
        add([1, 2], 3)


# проверка TypeError при неверных типах для subtract
@pytest.mark.feature('subtract')
def test_subtract_type_error():
    with pytest.raises(TypeError):
        subtract("5", 2)

    with pytest.raises(TypeError):
        subtract(5, "2")


# проверка TypeError при неверных типах для multiply
@pytest.mark.feature('multiply')
def test_multiply_type_error():
    with pytest.raises(TypeError):
        multiply("3", 5)

    with pytest.raises(TypeError):
        multiply(3, "5")


# проверка TypeError при неверных типах для divide
@pytest.mark.feature('divide')
def test_divide_type_error():
    with pytest.raises(TypeError):
        divide("10", 2)

    with pytest.raises(TypeError):
        divide(10, "2")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])