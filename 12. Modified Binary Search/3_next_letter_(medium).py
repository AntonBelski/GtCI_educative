def search_next_letter(letters, key):
    lo, hi = 0, len(letters)
    while lo != hi:
        mid = (lo + hi) // 2
        if key < letters[mid]:
            hi = mid
        else:
            lo = mid + 1

    return letters[lo % len(letters)]


def main():
    print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()
