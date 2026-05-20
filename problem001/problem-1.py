def character_replacement(s, k):
    freq = {}
    max_freq = 0
    left = 0
    max_length = 0
    for right in range(len(s)):
        char = s[right]
        freq[char] = freq.get(char, 0) + 1
        max_freq = max(max_freq, freq[char])
        while right - left + 1 - max_freq > k:
            freq[s[left]] -= 1
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length


print(character_replacement("AABABBABB", 1))  # Output: 4
