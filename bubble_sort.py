def bubble_sort(main_list: list) -> None:
    """
    Реализует алгорит "Пузырек"
    :param main_list: Исходный список элементов
    :return:
    """

    for i in range(len(main_list) - 1):
        for j in range(len(main_list) - 1 - i):
            if main_list[j] > main_list[j + 1]:
                main_list[j + 1], main_list[j] = main_list[j], main_list[j + 1]


if __name__ == '__main__':
    l = [0, 9, 8, 7, 6, 5, 4, 3]
    bubble_sort(l)
    print(l)
    