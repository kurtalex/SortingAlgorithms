def insertion_sort(lst):
    for item in range(1, len(lst)):
        current_value = lst[item]
        position = item

        while position > 0 and lst[position - 1] > current_value:
            lst[position] = lst[position - 1]
            position -= 1
        lst[position] = current_value

    return lst


lst = [12, 34, 25, 15, 67, 23, 11, 5, 86]
print("Исходный массив:", lst)
result = insertion_sort(lst)
print("Результат сортировки: ", result)
