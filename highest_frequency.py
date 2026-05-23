arr = [5, 5, 5, 2, 2, 2, 2, 2, 2, 2, 2]


def highest_frequency(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    max_freq = 0
    answer = None
    for key in freq:
        if freq[key] > max_freq:
            max_freq = freq[key]
            answer = key
    return answer


print(highest_frequency(arr))
