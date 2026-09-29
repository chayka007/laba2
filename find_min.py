"""Поиск минимального элемента списка без встроенного min()."""


def find_min(items):
    if not items:
        raise ValueError("Список пуст")
    minimum = items[0]
    for item in items[1:]:
        if item < minimum:
            minimum = item
    return minimum


if __name__ == "__main__":
    numbers = [8, 3, 12, -4, 7]
    print("Список:", numbers)
    print("Минимальный элемент:", find_min(numbers))
