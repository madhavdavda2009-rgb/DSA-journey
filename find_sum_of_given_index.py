arr = [4, 2, 7, 1, 5, 3]


def find_sum_of_given_index(arr, l, r):
    arr_sum = sum(arr[l : r + 1])
    return arr_sum


print(find_sum_of_given_index(arr, 1, 5))
