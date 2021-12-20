import math


# Вычисление последовательности Фибоначчи
def fibonacci(n, i=2, last=1, llast=0):
    if n == 0:
        return last
    elif n == 1:
        return llast

    llast, last = last, last + llast
    if n == i:
        return last
    else:
        return fibonacci(n, i+1, last, llast)


# Целевая функци
def f(x):
    return math.e ** x * math.sin(x)


# Определение количества иттераций для вычисления экстремума
def get_iter_count(val, i=2, last=1, llast=0):
    llast, last = last, last + llast
    if val > last:
        return get_iter_count(val, i+1, last, llast)
    else:
        return i


# Точность вычисления
eps = 0.01
# Отрезок для поиска минимума функции
min_range = [-1, 0]
# Отрезок для поиска максимума функции
max_range = [2, 3]
x_min, x_max = 0, 0

# Поиск минимума функции
a = min_range[0]
b = min_range[1]
# Необходимое количество иттераций для поиска минимума функции
iters = get_iter_count((b-a)/eps)

for k in range(1, iters-1):
    # Определение направления сжатия отрезка
    x1 = a + fibonacci(iters-k-1)/fibonacci(iters-k+1) * (b - a)
    x2 = a + fibonacci(iters-k)/fibonacci(iters-k+1) * (b - a)
    if f(x1) > f(x2):
        a = x1
        x1 = x2
        x2 = a + fibonacci(iters-k-1)/fibonacci(iters-k) * (b - a)
    else:
        b = x2
        x2 = x1
        x1 = a + fibonacci(iters-k-2)/fibonacci(iters-k) * (b - a)

x_min = (b+a)/2
y_min = f(x_min)


# Поиск максимума функции
a = max_range[0]
b = max_range[1]
# Необходимое количество иттераций для поиска максимума функции
iters = get_iter_count((b-a)/eps)
for k in range(1, iters-1):
    # Определение направления сжатия отрезка
    x1 = a + fibonacci(iters-k-1)/fibonacci(iters-k+1) * (b - a)
    x2 = a + fibonacci(iters-k)/fibonacci(iters-k+1) * (b - a)
    if f(x1) > f(x2):
        # Сжатие отрезка
        b = x2
        x2 = x1
        x1 = a + fibonacci(iters - k - 2) / fibonacci(iters - k) * (b - a)
    else:
        # Сжатие отрезка
        a = x1
        x1 = x2
        x2 = a + fibonacci(iters-k-1)/fibonacci(iters-k) * (b - a)
x_max = (b+a)/2
y_max = f(x_max)

# Вывод результата с точностью до тысячных
print(f"y_min={y_min:.3f}; x_min={x_min:.3f}")
print(f"y_max={y_max:.3f}; x_max={x_max:.3f}")



