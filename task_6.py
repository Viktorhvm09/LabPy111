# TODO 6.	Аренда ракет
#  Вы – компания, дающая в аренду ракеты. Каждый день к вам приходит список заявок на использование ракет в виде: (час_начала, час_конца), (час_начала, час_конца), ...
#  Если аренда ракеты заканчивается в час X, то в этот же час ее уже можно взять в аренду снова (т.е. час_начала может начинаться с Х).
#  Дано: список заявок на использование ракет
#  Задача: вывести ответ, хватит ли вам одной ракеты, чтобы удовлетворить все заявки на этот день

def rent_rocket(bookings):
    n = len(bookings)
    for i in range(n):
        for j in range(0, n - i - 1):
            if bookings[j][1] > bookings[j + 1][1]:
                bookings[j], bookings[j + 1] = bookings[j + 1], bookings[j]
    for i in range(1, len(bookings)):
        if bookings[i][0] < bookings[i - 1][1]:
            return False
    return True


if __name__ == "__main__":
    bookings = [(1, 4), (4, 6), (7, 9)]
    print(rent_rocket(bookings))  # True

    bookings = [(1, 4), (3, 6)]
    print(rent_rocket(bookings))  # False