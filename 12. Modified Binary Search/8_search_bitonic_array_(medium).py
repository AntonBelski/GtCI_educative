def binary_search_max(arr):
    lo, hi = 0, len(arr) - 1
    while lo != hi:
        mid = (lo + hi) // 2
        if arr[mid] > arr[mid + 1]:
            hi = mid
        else:
            lo = mid + 1
    return lo


def binary_search(arr, max_elem_ind, x, is_ascending=True):
    if is_ascending:
        lo, hi = 0, max_elem_ind
    else:
        lo, hi = 0, len(arr) - 1

    while lo != hi:
        mid = (lo + hi) // 2
        if x <= arr[mid] if is_ascending else x >= arr[mid]:
            hi = mid
        else:
            lo = mid + 1

    return lo


def search_bitonic_array(arr, x):
    max_elem_ind = binary_search_max(arr)

    left_ind = binary_search(arr, max_elem_ind, x)
    if arr[left_ind] == x:
        return left_ind

    right_ind = binary_search(arr, max_elem_ind, x, is_ascending=False)
    if arr[right_ind] == x:
        return right_ind
    else:
        return -1


def main():
    print(search_bitonic_array([1, 3, 8, 4, 3], 4))
    print(search_bitonic_array([3, 8, 3, 1], 8))
    print(search_bitonic_array([1, 3, 8, 12], 12))
    print(search_bitonic_array([10, 9, 8], 10))


main()
