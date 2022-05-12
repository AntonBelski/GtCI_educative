def find_string_anagrams(str1, pattern):
    pattern_dict = {}
    str1_dict = {}
    k = len(pattern)
    matches = 0
    result = []

    if k > len(str1):
        return result

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
        result.append(0)

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
            result.append(window_end - k + 1)

    return result


def main():
    print(find_string_anagrams("ppqp", "pq"))
    print(find_string_anagrams("abbcabc", "abc"))


main()
