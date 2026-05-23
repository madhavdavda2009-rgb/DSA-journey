arr = [4, 2, 7, 1, 5, 3]


def find_sum_of_given_index(arr, left, right):
    arr_sum = sum(arr[left : right + 1])
    return arr_sum


print(find_sum_of_given_index(arr, 1, 5))
