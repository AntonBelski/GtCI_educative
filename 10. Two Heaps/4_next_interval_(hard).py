from heapq import heapify, heappop


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def find_next_interval(intervals):
    start_heap, end_heap = [], []

    for i, pair in enumerate(intervals):
        start_heap.append([pair.start, i])
        end_heap.append([pair.end, i])

    heapify(start_heap)
    heapify(end_heap)

    results = [-1] * len(intervals)

    while end_heap:
        end, end_ind = heappop(end_heap)

        while start_heap and start_heap[0][0] < end:
            heappop(start_heap)

        if start_heap:
            results[end_ind] = start_heap[0][1]

    return results


def main():
    result = find_next_interval(
        [Interval(2, 3), Interval(3, 4), Interval(5, 6)])
    print("Next interval indices are: " + str(result))

    result = find_next_interval(
        [Interval(3, 4), Interval(1, 5), Interval(4, 6)])
    print("Next interval indices are: " + str(result))


main()
