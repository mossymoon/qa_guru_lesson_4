def test_greeting():
    """
    Напишите программу, которая выводит на экран приветствие.
    """
    name = "Анна"
    age = 25
    # TODO Сформируйте нужную строку
    output = f"Привет, {name}! Тебе {age} лет."
    # Проверяем результат
    assert output == "Привет, Анна! Тебе 25 лет."

def test_rectangle():
    """
    Напишите программу, которая берет длину и ширину прямоугольника
    и считает его периметр и площадь.
    """
    a = 10
    b = 20

    # TODO сосчитайте периметр
    perimeter = (10 + 20) * 2
    assert perimeter == 60

    # TODO сосчитайте площадь
    area = 10 * 20
    assert area == 200

def test_circle():
    import math
    """
    Напишите программу, которая берет радиус круга и выводит на экран его длину и площадь.
    Используйте константу PI
    """
    r = 23
    # TODO сосчитайте площадь
    area = math.pi * r ** 2
    assert math.floor(area) == math.floor(1661.9025137490005)

    # TODO сосчитайте длину окружности
    length = (math.pi * r) * 2
    assert math.floor(length) == math.floor(144.51326206513048)

def test_random_list():
    """
    Создайте список из 10 случайных чисел от 1 до 100 и отсортируйте его по возрастанию.
    """

    # TODO создайте список
    l = [2, 34, 68, 14, 87, 12, 4, 93, 65, 77]
    l.sort()
    assert len(l) == 10
    assert l[0] < l[-1]

def test_unique_elements():
    """
    Удалите из списка все повторяющиеся элементы
    """
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    # TODO удалите повторяющиеся элементы
    unique_l = set(l)
    l = list(unique_l)
    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_dicts():
    """
    Создайте словарь из двух списков.
    Используйте первый список как ключи, а второй - как значения.
    Выведите на экран все значения словаря.
    Подсказка: используй встроенную функцию zip.
    """
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    dict(zip(first, second))
    # TODO создайте словарь
    d = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5
    }

    assert isinstance(d, dict)
    assert len(d) == 5

