def longest_substring(s):
    freq = set()
    max_length = 0
    left = 0
    for right in range(len(s)):
        while s[right] in freq:
            freq.remove(s[left])
            left += 1
        freq.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length


print(longest_substring("abcabcbb"))  # Output: 3
