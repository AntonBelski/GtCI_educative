def longest_substring_with_k_distinct(str1, k):
    str1_counter = {}
    counter = 0
    longest_str = 0
    start_ind = 0
    for i in range(len(str1)):
        counter += 1
        if str1_counter.get(str1[i]):
            str1_counter[str1[i]] += 1
        else:
            str1_counter[str1[i]] = 1

        while len(str1_counter) > k:
            str1_counter[str1[start_ind]] -= 1
            if not str1_counter.get(str1[start_ind]):
                str1_counter.pop(str1[start_ind])
            start_ind += 1
            counter -= 1

        longest_str = max(longest_str, counter)
    return longest_str


def main():
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()