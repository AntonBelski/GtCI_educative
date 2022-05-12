def get_next(n):
    return sum([int(d) ** 2 for d in str(n)])


def find_happy_number(n):
    slow = n
    fast = n

    while fast != 1:
        slow = get_next(slow)
        fast = get_next(get_next(fast))

        if slow == fast and fast != 1:
            return False

    return True


def main():
    print(find_happy_number(23))
    print(find_happy_number(12))


main()
