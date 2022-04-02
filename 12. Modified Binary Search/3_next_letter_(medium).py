def search_next_letter(letters, key):
    lo = 0
    hi = len(letters) - 1

    while lo != hi:
        mid = (lo + hi) // 2
        if key >= letters[mid]:
            lo = mid + 1
        else:
            hi = mid

    if letters[lo] > key:
        return letters[lo]
    else:
        return letters[0]


def main():
    print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()
