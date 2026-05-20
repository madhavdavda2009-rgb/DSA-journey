# Problem 005 - Maximum Sum Subarray of Size K

## Problem Statement

Given:

- An array `nums`
- An integer `k`

Find the maximum sum of any contiguous subarray
of size `k`.

---

## Example

Input:

nums = [2,1,5,1,3,2]
k = 3

Output:

9

Explanation:

Possible windows:

[2,1,5] = 8
[1,5,1] = 7
[5,1,3] = 9
[1,3,2] = 6

Maximum sum:

9

Subarray:

[5,1,3]

---

# Definitions

## Array

A collection of ordered elements.

Example:

[1,2,3,4]

---

## Subarray

A continuous part of an array.

Example:

[2,3]

is a subarray of:

[1,2,3,4]

---

## Sliding Window

A technique where we move a window through an array
without recalculating everything.

Example:

[2,1,5]
 [1,5,1]
  [5,1,3]

---

## Fixed Size Sliding Window

The window size never changes.

Formula:

window size = k

---

## Rolling Sum

Updating sum efficiently.

Formula:

new_sum = old_sum + new_element - removed_element

This avoids recalculating full sum.

---

## Negative Infinity

float('-inf')

Represents smallest possible value.

Useful when finding maximum.

---

# Brute Force Approach

Check every subarray of size k

For each:

- Calculate sum
- Compare with maximum

Time Complexity:

O(n*k)

Space Complexity:

O(1)

---

# Optimal Approach (Sliding Window)

## Step 1

Create first window sum

Store in:

current_sum

---

## Step 2

Store max sum

max_sum = current_sum

---

## Step 3

Slide window

Add new right element

Remove old left element

---

## Step 4

Update max

max_sum = max(max_sum, current_sum)

---

# Code Explanation

## Edge Case Check

if not arr or k <= 0:
    return 0

Handles invalid input

---

## Initialize max sum

max_sum = float('-inf')

Stores largest sum found

---

## Current sum

current_sum = 0

Tracks window sum

---

## Start pointer

start = 0

Beginning of window

---

## Expand window

for end in range(len(arr))

Moves window forward

---

## Add element

current_sum += arr[end]

Adds current number

---

## Fixed size check

if end - start + 1 == k

Formula:

window size = end - start + 1

Checks if window reached size k

---

## Update max

max_sum = max(max_sum, current_sum)

Stores best answer

---

## Remove left element

current_sum -= arr[start]

Shrinks old window

---

## Move start

start += 1

Slides window

---

# Complexity Analysis

Time Complexity:

O(n)

Each element visited once

---

Space Complexity:

O(1)

No extra memory used

---

# Common Mistakes

Wrong:

Recalculate sum(window) every time

Slow:

O(n*k)

Correct:

Use rolling sum

O(n)

---

Wrong:

Forget to remove left element

Window becomes invalid

Correct:

current_sum -= arr[start]

---

Wrong:

Wrong window size formula

Correct:

end - start + 1

---

# Key Learning

- Fixed-size sliding window
- Rolling sum optimization
- Window shifting
- Efficient maximum tracking

---

# Final Code

def max_subarray_sum_of_size_k(arr, k):
    if not arr or k <= 0:
        return 0

    max_sum = float('-inf')
    current_sum = 0
    start = 0

    for end in range(len(arr)):
        current_sum += arr[end]

        if end - start + 1 == k:
            max_sum = max(max_sum, current_sum)
            current_sum -= arr[start]
            start += 1

    return max_sum


print(max_subarray_sum_of_size_k([2,1,5,1,3,2],3))