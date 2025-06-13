def factorial_recursive(n: int) -> int:
    """
    Рассчитать факториал числа n рекурсивным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    ...  # TODO реализовать рекурсивный алгоритм нахождения факториала
    if n < 0:
        raise ValueError("Не должно быть меньше 0")
    if not isinstance(n, int):
        raise TypeError("Только целое число")

    if n == 0:
        return 1
    return factorial_recursive(n-1) * n