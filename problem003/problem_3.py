def min_subarray_sum(arr, k):
    min_length = float("inf")
    current_sum = 0
    left = 0
    for right in range(len(arr)):
        current_sum += arr[right]
        while current_sum >= k:
            min_length = min(min_length, right - left + 1)
            current_sum -= arr[left]
            left += 1
    return min_length if min_length != float("inf") else 0


print(min_subarray_sum([1, 2, 3, 4, 5], 11))
