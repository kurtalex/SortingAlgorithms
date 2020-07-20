def selection_sort(lst):
    for num in range(len(lst)):
        min_value = num

        for item in range(num, len(lst)):
            if lst[min_value] > lst[item]:
                min_value = item

        lst[num], lst[min_value] = lst[min_value], lst[num]

    return lst


lst = [12, 34, 25, 15, 67, 23, 11, 5, 86]
print("Исходный массив: ", lst)

result = selection_sort(lst)

print("Результат сортировки: ", result)
