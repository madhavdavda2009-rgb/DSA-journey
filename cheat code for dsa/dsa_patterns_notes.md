# DSA Core Patterns Notes

## 1. Loop Traversal
Use:
```python
for item in arr:
```

Kaam:
- Sum
- Max/min
- Counting

Pattern:
Initialize → Traverse → Check → Update

---

## 2. Frequency Map
```python
freq[item] = freq.get(item, 0) + 1
```

Use:
- Count frequency
- Duplicate detect
- Most frequent

---

## 3. Two Pointer
```python
left = 0
right = len(arr)-1
while left < right:
```

Use:
- Palindrome
- Pair sum
- Reverse

---

## 4. Sliding Window
```python
left = 0
for right in range(len(arr)):
```

Use:
- Longest substring
- Fixed-size subarray

Update:
```python
max_len = max(max_len, right-left+1)
```

---

## 5. Prefix Sum
```python
prefix[i]=prefix[i-1]+arr[i]
```

Use:
Fast range sum queries.

---

## 6. Set
```python
seen=set()
```

Use:
- Duplicate checking
- Unique values

---

## 7. Greedy
Choose best local option.

Usually:
```python
arr.sort()
```

Use:
Optimization problems.

---

## 8. Binary Search
```python
left=0
right=len(arr)-1
while left<=right:
    mid=(left+right)//2
```

Use:
Sorted array search

Time:
O(log n)

---

# Universal Framework

1. Initialize
2. Iterate
3. Check
4. Update
5. Return

---

# Question Signals

Count → Dictionary  
Duplicate → Set  
Continuous → Sliding Window  
Opposite compare → Two Pointer  
Sorted fast search → Binary Search  
Repeated sum → Prefix Sum  
Best choice → Greedy

---

# Golden Rule
DSA = Pattern Recognition
