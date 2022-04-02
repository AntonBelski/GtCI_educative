def search_ceiling_of_a_number(arr, k):
    lo = 0
    hi = len(arr) - 1

    while lo != hi:
        mid = (lo + hi) // 2
        if k <= arr[mid]:
            hi = mid
        else:
            lo = mid + 1

    if arr[lo] >= k:
        return lo
    elif lo != len(arr) - 1:
        return lo + 1
    else:
        return -1


def search_floor_of_a_number(arr, k):
    lo = 0
    hi = len(arr) - 1

    while lo != hi:
        mid = (lo + hi) // 2
        if k <= arr[mid]:
            hi = mid
        else:
            lo = mid + 1

    if arr[lo] <= k:
        return lo
    else:
        return lo - 1


def main():
    print(search_ceiling_of_a_number([4, 6, 10], 6))
    print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_ceiling_of_a_number([4, 6, 10], 17))
    print(search_ceiling_of_a_number([4, 6, 10], -1))
    print()
    print(search_floor_of_a_number([4, 6, 10], 6))
    print(search_floor_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_floor_of_a_number([4, 6, 10], 17))
    print(search_floor_of_a_number([4, 6, 10], -1))


main()
