def remove_duplicates(arr):
    if not arr:
        return 0

    prev_elem = arr[0]
    duplicates = 0

    for elem in arr[1:]:
        if elem == prev_elem:
            duplicates += 1
        prev_elem = elem

    return len(arr) - duplicates


def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))


main()
