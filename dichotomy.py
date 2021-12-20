import math


# Центр отрезка
def get_center(curr_range: list) -> float:
    return sum(curr_range)/2


# Целевая функци
def f(x):
    return math.e ** x * math.sin(x)


# Точность вычисления
eps = 0.01
# Отрезок для поиска минимума функции
min_range = [-1, 0]
# Отрезок для поиска максимума функции
max_range = [2, 3]
x_min, x_max = 0, 0

# Поиск минимума функции
# Центр отрезка
center = get_center(min_range)
while True:
    # Определяем направление сжатия отрезка
    x_1 = center - eps
    x_2 = center + eps
    if f(x_1) > f(x_2):
        # Сжатие отрезка
        min_range = [center, min_range[1]]
        x_min = x_2
    else:
        # Сжатие отрезка
        min_range = [min_range[0], center]
        x_min = x_1

    new_center = get_center(min_range)
    # Останавливаемся если отрезок меньше заданной точности
    if math.fabs(new_center-center) <= eps:
        break
    else:
        center = new_center

# Поиск максимума функции
# Центр отрезка
center = get_center(max_range)
while True:
    # Определяем направление сжатия отрезка
    x_1 = center - eps
    x_2 = center + eps
    if f(x_2) > f(x_1):
        # Сжатие отрезка
        max_range = [center, max_range[1]]
        x_max = x_2
    else:
        # Сжатие отрезка
        max_range = [max_range[0], center]
        x_max = x_1

    new_center = get_center(max_range)
    # Останавливаемся если отрезок меньше заданной точности
    if math.fabs(new_center-center) <= eps:
        break
    else:
        center = new_center

# Вывод результата с точностью до тысячных
print(f"y_min={f(x_min):.3f}; x_min={x_min:.3f}")
print(f"y_max={f(x_max):.3f}; x_max={x_max:.3f}")