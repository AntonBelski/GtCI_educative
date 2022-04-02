def binary_search(arr, key):
    is_ascending = arr[0] <= arr[len(arr) - 1]
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        if arr[lo] == key:
            return lo

        mid = (lo + hi) // 2
        if is_ascending and key < arr[mid] or not is_ascending and key > arr[mid]:
            hi = mid - 1
        elif is_ascending and key > arr[mid] or not is_ascending and key < arr[mid]:
            lo = mid + 1
        else:
            return mid

    return -1


def main():
    print(binary_search([4, 6, 10], 10))
    print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
    print(binary_search([10, 6, 4], 10))
    print(binary_search([10, 6, 4], 4))


main()
