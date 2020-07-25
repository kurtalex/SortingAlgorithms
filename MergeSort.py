def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    middle = len(lst) // 2
    left_list = lst[:middle]
    right_list = lst[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    return list(merge(left_list, right_list))


def merge(left_half, right_half):
    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res += right_half
    else:
        res += left_half
    return res


lst = [12, 34, 25, 15, 67, 23, 11, 5, 86]
print("Исходный массив: ", lst)
result = merge_sort(lst)
print("Результат сортировки: ", result)
