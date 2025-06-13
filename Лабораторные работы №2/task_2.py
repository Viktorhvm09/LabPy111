import math


def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    ...  # TODO реализовать итеративный алгоритм нахождения факториала
    if n < 0:
        raise ValueError("Меньше 0")

    factorial = 0
    for i in range(0, n+1):
        if i < 2:
            factorial = 1
        else:
            factorial *= i

    return factorial