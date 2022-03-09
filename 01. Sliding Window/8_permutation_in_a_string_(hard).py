def find_permutation(str1, pattern):
    pattern_dict = {}
    str1_dict = {}
    k = len(pattern)
    matches = 0

    if k > len(str1):
        return False

    for i in range(ord('a'), ord('z') + 1):
        pattern_dict[chr(i)] = 0
        str1_dict[chr(i)] = 0

    for i in range(k):
        pattern_dict[pattern[i]] += 1
        str1_dict[str1[i]] += 1

    for i in range(ord('a'), ord('z') + 1):
        if pattern_dict[chr(i)] == str1_dict[chr(i)]:
            matches += 1

    if matches == 26:
        return True

    for window_end in range(k, len(str1)):
        window_end_elem = str1[window_end]
        str1_dict[window_end_elem] += 1
        if str1_dict[window_end_elem] == pattern_dict[window_end_elem]:
            matches += 1
        elif str1_dict[window_end_elem] - 1 == pattern_dict[window_end_elem]:
            matches -= 1

        window_start_elem = str1[window_end - k]
        str1_dict[window_start_elem] -= 1
        if str1_dict[window_start_elem] == pattern_dict[window_start_elem]:
            matches += 1
        elif str1_dict[window_start_elem] + 1 == pattern_dict[window_start_elem]:
            matches -= 1

        if matches == 26:
            return True

    return False


def main():
    print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
    print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
    print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
    print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))


main()
