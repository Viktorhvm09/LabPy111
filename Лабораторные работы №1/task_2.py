def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    # TODO реализовать проверку скобочной группы
    list_ = []
    for i in brackets_row:
        if i == '(':
            list_.append(i)
        elif i == ')':
            if not list_:
                return False
            list_.pop()
    return len(list_) == 0

if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
