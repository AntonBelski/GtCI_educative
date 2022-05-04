from __future__ import print_function
from heapq import heapify, heappop, heappush


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def find_employee_free_time(schedule):
    result = []
    heap = [[e[0].start, e[0].end, i, 0] for i, e in enumerate(schedule)]
    heapify(heap)
    prev_end = heap[0][1]

    while heap:
        start, end, emp_i, i = heappop(heap)
        if i + 1 < len(schedule[emp_i]):
            next_start = schedule[emp_i][i + 1].start
            next_end = schedule[emp_i][i + 1].end
            next_event = [next_start, next_end, emp_i, i + 1]
            heappush(heap, next_event)

        if start > prev_end:
            result.append(Interval(prev_end, start))
        prev_end = max(prev_end, end)

    return result


def main():
    input = [[Interval(1, 3), Interval(5, 6)], [
        Interval(2, 3), Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3), Interval(9, 12)], [
        Interval(2, 4)], [Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3)], [
        Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()


main()
