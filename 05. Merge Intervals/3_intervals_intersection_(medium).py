def merge(fl, sl):
    result = []
    p1, p2 = 0, 0

    while p1 < len(fl) and p2 < len(sl):
        max_start = max(fl[p1][0], sl[p2][0])
        min_end = min(fl[p1][1], sl[p2][1])

        if min_end >= max_start:
            result.append([max_start, min_end])

        if fl[p1][1] > sl[p2][1]:
            p2 += 1
        else:
            p1 += 1

    return result


def main():
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()
