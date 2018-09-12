import time


def timing(fun):
    def wrapper(*args, **kwargs):
        start = time.time()
        a = fun(*args, **kwargs)
        end = time.time()
        print('time:{}'.format(end - start))
        return a
    return wrapper


def partition(array, first_index, last_index):
    i = first_index - 1
    for j in range(first_index, last_index):
        if array[j] <= array[last_index]:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[last_index] = array[last_index], array[i + 1]
    return i


def quick_sort(array, first_index, last_index):
    if first_index < last_index:
        div_index = partition(array, first_index, last_index)
        quick_sort(array, first_index, div_index)
        quick_sort(array, div_index + 1, last_index)
    else:
        return


@timing
def quick_sort_2(array, left, right):
    if left >= right:
        return
    low = left
    high = right
    key = array[low]
    while left < right:
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
    array[right] = key
    quick_sort_2(array, low, left - 1)
    quick_sort_2(array, left + 1, high)


arr = [1, 4, 7, 1, 5, 5, 3, 85, 34, 75, 23, 75, 2, 0]
quick_sort_2(arr, 0, len(arr) - 1)
print(arr)
