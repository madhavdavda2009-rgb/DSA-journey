"""# Problem 001 - Longest Repeating Character Replacement

## Problem Statement
Given a string s and integer k,
replace at most k characters to get the longest substring containing same characters.

---

## Definitions

### Sliding Window
A technique where a window/subarray moves through the string or array.

### Frequency Map
Dictionary storing frequency of elements.

### Window Size
right - left + 1

### Max Frequency
Highest frequency character inside current window.

---

## Brute Force Approach

Generate all substrings.
Check replacements needed for every substring.

Time Complexity: O(n²)

---

## Optimal Approach

Use sliding window.

Track:
- character frequencies
- maximum frequency

If:
(window size - max frequency) > k

Shrink window from left.

---

## Complexity

Time Complexity: O(n)

Space Complexity: O(1)

---

## Key Learning

We only care whether required replacements are <= k."""