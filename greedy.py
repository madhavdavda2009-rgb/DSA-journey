arr = [20, 10, 5, 2, 1]


def greedy(arr, target):
    list1 = []
    for num in arr:
        while target >= num:
            target -= num
            list1.append(num)
    return list1


print(greedy(arr, 38))
