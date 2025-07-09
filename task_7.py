# TODO 7.	Сорт
#  Дано: массив из 10**6 целых чисел, каждое из которых лежит на отрезке [13, 25].
#  Задача: отсортировать массив наиболее эффективным способом.

def counting_sort(arr):
    min_val = 13
    max_val = 25
    count = [0] * (max_val - min_val + 1)

    for num in arr:
        count[num - min_val] += 1

    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i + min_val] * count[i])

    return sorted_arr


if __name__ == "__main__":
    import random

    arr = [random.randint(13, 25) for _ in range(10 ** 6)]
    sorted_arr = counting_sort(arr)
    print(sorted_arr)