def quick_sort(lst):
    quick_sort_helper(lst, 0, len(lst) - 1)
    return lst


def quick_sort_helper(lst, low, high):
    if low < high:
        split_point = partition(lst, low, high)
        quick_sort_helper(lst, low, split_point - 1)
        quick_sort_helper(lst, split_point + 1, high)


def partition(lst, low, high):
    pivot_value = lst[low]
    left_mark = low + 1
    right_mark = high
    done = False

    while not done:
        while left_mark <= right_mark and lst[left_mark] <= pivot_value:
            left_mark += 1
        while right_mark >= left_mark and lst[right_mark] >= pivot_value:
            right_mark -= 1

        if right_mark < left_mark:
            done = True
        else:
            lst[left_mark], lst[right_mark] = lst[right_mark], lst[left_mark]

    lst[low], lst[right_mark] = lst[right_mark], lst[low]
    return right_mark


lst = [19, 2, 31, 45, 6, 11, 121, 27]
print("Исходный массив: ", lst)
result = quick_sort(lst)
print("Результат сортировки:", result)
