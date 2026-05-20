# Problem 003 - Minimum Size Subarray Sum

## Problem Statement

Given:

- An integer `target`
- An array of positive integers `nums`

Return the minimum length of a contiguous subarray
whose sum is greater than or equal to target.

If no such subarray exists, return `0`.

---

## Example

Input:

target = 7
nums = [2,3,1,2,4,3]

Output:

2

Explanation:

Subarray:

[4,3]

Sum:

4 + 3 = 7

Length:

2

This is the smallest valid subarray.

---

# Definitions

## Array
A collection of elements stored in order.

Example:

[1,2,3,4]

---

## Subarray
A continuous part of an array.

Example:

[2,3]

is a subarray of:

[1,2,3,4]

But:

[1,3]

is NOT a subarray because it is not continuous.

---

## Sliding Window
A technique where we maintain a moving window
instead of checking all subarrays.

Example:

[1,2]
 [2,3]
  [3,4]

This improves efficiency.

---

## Running Sum

The total sum of elements inside the current window.

Example:

[2,3,1]

Running sum:

2 + 3 + 1 = 6

---

## Window Size

Formula:

window size = right - left + 1

---

## Infinity

float('inf')

Represents a very large number.

Used when searching for minimum values.

---

# Brute Force Approach

Generate all possible subarrays.

For each:

- Calculate sum
- Check if sum >= target
- Store smallest length

Time Complexity:

O(n²)

Space Complexity:

O(1)

---

# Optimal Approach (Sliding Window)

## Step 1

Expand window using right pointer.

Add current number:

current_sum += nums[right]

---

## Step 2

Check validity

If:

current_sum >= target

Window is valid.

---

## Step 3

Try shrinking from left

Why?

To find the smallest valid window.

Remove:

current_sum -= nums[left]

Move:

left += 1

---

## Step 4

Update minimum length

Formula:

min_length = min(min_length, right-left+1)

---

# Code Explanation

## Create minimum tracker

min_length = float('inf')

Stores smallest valid length

---

## Current window sum

current_sum = 0

Tracks sum of current window

---

## Left pointer

left = 0

Window starting position

---

## Expand window

for right in range(len(nums))

Moves window forward

---

## Add number

current_sum += nums[right]

Updates running sum

---

## Valid check

while current_sum >= target

Means current window satisfies condition

---

## Update answer

min_length = min(min_length, right-left+1)

Stores smallest valid length

---

## Shrink window

current_sum -= nums[left]
left += 1

Makes window smaller

---

## Final return

If no valid subarray exists:

return 0

Otherwise:

return min_length

---

# Complexity Analysis

Time Complexity:

O(n)

Why:

Each element is visited at most twice
(one by right pointer, one by left pointer)

---

Space Complexity:

O(1)

No extra memory used

---

# Common Mistake

Wrong:

min(min_length, current_sum)

This compares sums ❌

Correct:

min(min_length, right-left+1)

This compares lengths ✅

---

# Key Learning

- Sliding window works when numbers are positive
- Expand until valid
- Shrink to optimize
- Track minimum length, not minimum sum

---

# Final Code

def min_subarray_sum(arr, k):
    min_length = float('inf')
    current_sum = 0
    left = 0

    for right in range(len(arr)):
        current_sum += arr[right]

        while current_sum >= k:
            min_length = min(min_length, right-left+1)

            current_sum -= arr[left]
            left += 1

    return min_length if min_length != float('inf') else 0


print(min_subarray_sum([1,2,3,4,5],11))