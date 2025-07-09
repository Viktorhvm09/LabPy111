# TODO 2.	Считалочка Дано N человек, считалка из K слогов.
#  Считалка начинает считать с первого человека. Когда считалка досчитывает до k-го слога,
#  человек, на котором она остановилась, вылетает. Игра происходит до тех пор,
#  пока не останется последний человек. Для данных N и К дать номер последнего
#  оставшегося человека.

def last_person(N, K):
    person = list(range(1, N + 1))
    index = 0
    while len(person) > 1:
        for _ in range(K - 1):
            index += 1
            if index >= len(person):
                index = 0
        person.pop(index)
        if index >= len(person):
            index = 0
    return person[0]


if __name__ == '__main__':
    print(last_person(5, 2)) # 3
    print(last_person(2, 2)) # 1
    print(last_person(3, 2)) # 3