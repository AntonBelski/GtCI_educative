def non_repeat_substring(str1):
    start_ind = 0
    counter = 0
    max_counter = 0
    str1_dict = {}
    for ch in str1:
        counter += 1
        if str1_dict.get(ch):
            str1_dict[ch] += 1
            while str1_dict[ch] > 1:
                str1_dict[str1[start_ind]] -= 1
                if not str1_dict[str1[start_ind]]:
                    str1_dict.pop(str1[start_ind])
                counter -= 1
                start_ind += 1
        else:
            str1_dict[ch] = 1

        max_counter = max(counter, max_counter)
    return max_counter


def main():
    print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abccde")))


main()
