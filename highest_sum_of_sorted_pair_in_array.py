arr = [1, 3, 4, 6, 8, 10]


def sorted_pair_sum(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return False


print(sorted_pair_sum(arr, 14))
