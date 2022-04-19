def insert(intervals, new_interval):
    result = []
    start = 0
    n = len(intervals)

    while start < n and intervals[start][1] < new_interval[0]:
        result.append(intervals[start])
        start += 1

    result.append(new_interval)
    while start < n and result[-1][1] >= intervals[start][0]:
        result[-1] = [min(result[-1][0], intervals[start][0]),
                      max(result[-1][1], intervals[start][1])]
        start += 1

    while start < n:
        result.append(intervals[start])
        start += 1

    return result


def main():
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()
