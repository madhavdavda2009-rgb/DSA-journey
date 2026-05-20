# Problem 004 - Permutation in String

## Problem Statement

Given two strings:

- s1
- s2

Return True if s2 contains a permutation of s1.

Otherwise return False.

---

## Example 1

Input:

s1 = "ab"
s2 = "eidbaooo"

Output:

True

Explanation:

"ba" exists in s2

"ba" is a permutation of "ab"

---

## Example 2

Input:

s1 = "ab"
s2 = "eidboaoo"

Output:

False

No permutation exists.

---

# Definitions

## Permutation

A rearrangement of characters.

Example:

Permutation of:

"abc"

can be:

"bac"
"cab"
"cba"

Characters same,
order different.

---

## Frequency Map

A dictionary storing frequency of characters.

Example:

"abb"

Frequency map:

{
 'a':1,
 'b':2
}

---

## Sliding Window

A moving window over a string or array.

Example:

[ab]
 [bc]
  [cd]

This avoids checking all substrings manually.

---

## Fixed Size Sliding Window

A sliding window whose size never changes.

For this problem:

window size = len(s1)

Every step:

- Add one character to right
- Remove one character from left

---

## Dictionary Equality

Two dictionaries are equal if:

- Same keys
- Same values

Example:

{'a':1,'b':2} == {'b':2,'a':1}

Result:

True

Order does not matter.

---

# Brute Force Approach

Generate every substring of length len(s1)

For each:

- Build frequency map
- Compare with s1 frequency map

If equal:

Return True

Otherwise:

Return False

Time Complexity:

O(n * m)

Where:

n = length of s2
m = length of s1

---

# Optimal Approach

## Step 1

Create frequency map for s1

freq1

---

## Step 2

Create frequency map for first window of s2

freq2

Window size:

len(s1)

---

## Step 3

Compare

If:

freq1 == freq2

Return True

---

## Step 4

Slide window

Add new right character

Remove old left character

If frequency becomes zero:

Delete that key

---

## Step 5

Compare again

If equal:

Return True

---

## Step 6

If no match found

Return False

---

# Code Explanation

## Length check

if len(s1) > len(s2):
    return False

Permutation impossible.

---

## Build first frequency map

freq1[char] = freq1.get(char,0)+1

Stores s1 frequency.

---

## Build first window

for i in range(len(s1))

Creates first window frequency map.

---

## Compare first window

if freq1 == freq2:
    return True

---

## Slide window

Add:

freq2[s2[right]] += 1

Remove:

freq2[s2[left]] -= 1

---

## Delete zero frequency

if freq2[s2[left]] == 0:
    del freq2[s2[left]]

Why?

Because:

{'a':0} != {}

---

## Move left

left += 1

---

## Compare again

if freq1 == freq2:
    return True

---

# Complexity Analysis

Time Complexity:

O(n)

Each character processed once

---

Space Complexity:

O(1)

At most 26 lowercase letters

---

# Common Mistakes

Wrong:

Comparing whole s2 frequency

Correct:

Compare each window frequency

---

Wrong:

Using zip(freq1,freq2)

Dictionary order is unreliable

Correct:

freq1 == freq2

---

Wrong:

Returning inside first loop iteration

This stops checking early

Correct:

Return only after full comparison

---

# Key Learning

- Fixed-size sliding window
- Dictionary comparison
- Frequency tracking
- Delete zero-frequency keys
- Compare windows efficiently

---

# Final Code

def permutation_str(s1, s2):

    if len(s1) > len(s2):
        return False

    freq1 = {}
    freq2 = {}

    for char in s1:
        freq1[char] = freq1.get(char, 0) + 1

    for i in range(len(s1)):
        freq2[s2[i]] = freq2.get(s2[i], 0) + 1

    if freq1 == freq2:
        return True

    left = 0

    for right in range(len(s1), len(s2)):

        freq2[s2[right]] = freq2.get(s2[right], 0) + 1

        freq2[s2[left]] -= 1

        if freq2[s2[left]] == 0:
            del freq2[s2[left]]

        left += 1

        if freq1 == freq2:
            return True

    return False


print(permutation_str("ab","eidbaooo"))