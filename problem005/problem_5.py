def max_subarray_sum_of_size_k(arr, k):
    if not arr or k <= 0:
        return 0

    max_sum = float("-inf")
    current_sum = 0
    start = 0

    for end in range(len(arr)):
        current_sum += arr[end]

        if end - start + 1 == k:
            max_sum = max(max_sum, current_sum)
            current_sum -= arr[start]
            start += 1

    return max_sum


print(max_subarray_sum_of_size_k([2, 1, 5, 1, 3, 2], 3))
