# Problem 002 - Longest Substring Without Repeating Characters

## Problem Statement

Given a string `s`, find the length of the longest substring
without repeating characters.

Example:

Input:
s = "abcabcbb"

Output:
3

Explanation:
The answer is "abc", length = 3


---

# Definitions

## Substring
A continuous part of a string.

Example:
"abc" is a substring of "abcdef"

"ace" is NOT a substring because it is not continuous.


---

## Sliding Window
A technique where we maintain a moving window
over the string or array instead of checking all substrings.

Example:

[abc]
 [bca]
  [cab]


---

## Set
A collection that stores unique elements only.

Example:

{'a', 'b', 'c'}

Duplicate values are not allowed.


---

## Left Pointer
Marks the start of the current window.

Example:

abcabc
^

left = 0


---

## Right Pointer
Marks the end of the current window.

Example:

abcabc
  ^

right = 2


---

## Window Size

Formula:

window size = right - left + 1


---

# Brute Force Approach

Generate all possible substrings.

For each substring:
- Check if all characters are unique
- Update maximum length

Time Complexity:
O(n²)

Space Complexity:
O(n)


---

# Optimal Approach (Sliding Window + Set)

Steps:

1. Create a set to store unique characters
2. Expand window using right pointer
3. If duplicate found:
   - Remove characters from left
   - Move left forward
4. Add current character
5. Update max length


---

# Code Explanation

## Create set

freq = set()

Stores unique characters in current window


---

## Track longest length

max_length = 0


---

## Start window

left = 0


---

## Expand window

for right in range(len(s))

Moves right pointer through string


---

## Duplicate check

while s[right] in freq

If duplicate exists,
window becomes invalid


---

## Shrink window

freq.remove(s[left])
left += 1

Remove left character until duplicate gone


---

## Add new character

freq.add(s[right])


---

## Update answer

max_length = max(max_length, right-left+1)


---

# Complexity Analysis

Time Complexity:
O(n)

Why:
Each character is visited at most twice
(one by right, one by left)

Space Complexity:
O(min(n, m))

Where:
n = length of string
m = number of unique characters


---

# Key Learning

- Sliding window avoids checking all substrings
- Set helps detect duplicates quickly
- Shrink window only when invalid
- Always update longest valid window


---

# Final Code

def longest_substring(s):
    freq = set()
    max_length = 0
    left = 0

    for right in range(len(s)):
        while s[right] in freq:
            freq.remove(s[left])
            left += 1

        freq.add(s[right])
        max_length = max(max_length, right-left+1)

    return max_length


print(longest_substring("abcabcbb"))