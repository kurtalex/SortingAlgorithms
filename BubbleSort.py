def bubble_sort(lst):
    for num in range(len(lst) - 1, 0, -1):
        for item in range(num):
            if lst[item] > lst[item + 1]:
                lst[item], lst[item + 1] = lst[item + 1], lst[item]

    return lst


lst = [12, 34, 25, 15, 67, 23, 11, 5, 86]
print("Исхожный массив: ", lst)
result = bubble_sort(lst)
print("Результат сортировки:", result)
