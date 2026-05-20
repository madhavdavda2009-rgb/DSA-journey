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


print(permutation_str("ab", "eida"))