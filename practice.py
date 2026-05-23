arr = [12, 32, 43, 54, 65, 76, 87, 98]
largest_odd = arr[0]
for num in arr:
    if num % 2 != 0 and num > largest_odd:
        largest_odd = num
print(largest_odd)
