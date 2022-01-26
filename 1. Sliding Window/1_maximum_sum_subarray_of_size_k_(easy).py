def max_sub_array_of_size_k(k, arr):
    curr_max = sum(arr[:k])
    arr_max = curr_max
    for i in range(k, len(arr)):
        curr_max += arr[i] - arr[i - k]
        if curr_max > arr_max:
            arr_max = curr_max
    return arr_max


def main():
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))


main()