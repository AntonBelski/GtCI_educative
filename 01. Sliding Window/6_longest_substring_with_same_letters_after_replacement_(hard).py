def length_of_longest_substring(str1, k):
    s_dict = {}
    max_ch = 0
    start_ind = 0
    for i in range(len(str1)):
        c = str1[i]
        if s_dict.get(c):
            s_dict[c] += 1
        else:
            s_dict[c] = 1

        max_ch = max(max_ch, s_dict[c])

        if i + 1 - start_ind > max_ch + k:
            s_dict[str1[start_ind]] -= 1
            start_ind += 1

    return min(len(str1), k + max_ch)


def main():
    print(length_of_longest_substring("aabccbb", 2))
    print(length_of_longest_substring("abbcb", 1))
    print(length_of_longest_substring("abccde", 1))


main()
