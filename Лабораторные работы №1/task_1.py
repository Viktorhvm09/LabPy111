"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        TODO Описать где начало и конец очереди
        индекс 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.
        """
        # TODO инициализировать список
        self.queue = []

    def enqueue(self, elem: Any) -> None: #O(1)
        """
        Добавление элемент в конец очереди

        :param elem: Элемент, который должен быть добавлен
        """
        # TODO реализовать метод enqueue
        self.queue.append(elem)

    def dequeue(self) -> Any: #O(1)
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        # TODO реализовать метод dequeue
        if not self.queue:
            raise IndexError("Извлечение из пустого списка не возможно")

        return self.queue.pop(0)

    def peek(self, ind: int = 0) -> Any: #O(1)
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        # TODO реализовать метод peek
        if not isinstance(ind, int):
            raise TypeError(f"Индекс должен быть целочисленного типа, а не {type(ind).__name__}")

        if not 0 <= ind < len(self.queue):
            raise IndexError("Индекс все границ очереди")

        return self.queue[ind]

    def clear(self) -> None: #O(1)
        """ Очистка очереди. """
        # TODO реализовать метод clear
        self.queue.clear()

    def __len__(self): #O(1)
        """ Количество элементов в очереди. """
        # TODO реализовать метод __len__
        return len(self.queue)
