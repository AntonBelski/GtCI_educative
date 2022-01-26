from math import inf


def smallest_subarray_sum(s, arr):
    arr_len = 0
    start_ind = 0
    arr_sum = 0
    min_arr_len = inf
    for i in range(len(arr)):
        arr_sum += arr[i]
        arr_len += 1
        while arr_sum >= s and arr_len > 0:
            min_arr_len = min(arr_len, min_arr_len)
            arr_sum -= arr[start_ind]
            start_ind += 1
            arr_len -= 1

    return 0 if min_arr_len > len(arr) else min_arr_len


def main():
    print("Smallest subarray length: " + str(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(smallest_subarray_sum(8, [3, 4, 1, 1, 6])))


main()