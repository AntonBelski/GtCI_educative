from __future__ import print_function


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge(intervals):
    results = []
    intervals.sort(key=lambda k: k.start)

    start = intervals[0].start
    end = intervals[0].end

    for interval in intervals[1:]:
        curr_start = interval.start
        curr_end = interval.end
        if curr_start > end:
            results.append(Interval(start, end))
            start = curr_start
            end = curr_end
        else:
            end = max(end, curr_end)

    results.append(Interval(start, end))

    return results


def main():
    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()


main()
