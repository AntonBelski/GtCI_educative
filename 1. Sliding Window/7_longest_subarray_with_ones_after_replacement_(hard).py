def length_of_longest_substring(arr, k):
    ones_counter = 0
    start_ind = 0
    max_counter = 0

    for i in range(len(arr)):
        if arr[i] == 1:
            ones_counter += 1

        if i + 1 - start_ind > ones_counter + k:
            if arr[start_ind] == 1:
                ones_counter -= 1
            start_ind += 1

        max_counter = max(max_counter, i + 1 - start_ind)

    return max_counter


def main():
    print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


main()
