from heapq import heappop, heappush


class Job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load


def find_max_cpu_load(jobs):
    pairs = sorted(jobs, key=lambda x: x.start)
    cpu_load, max_cpu_load = pairs[0].cpu_load, pairs[0].cpu_load
    heap = [[pairs[0].end, pairs[0].cpu_load]]

    for pair in pairs[1:]:
        heappush(heap, [pair.end, pair.cpu_load])
        cpu_load += pair.cpu_load
        while heap and heap[0][0] <= pair.start:
            cpu_load -= heappop(heap)[1]

        max_cpu_load = max(cpu_load, max_cpu_load)

    return max_cpu_load


def main():
    print("Maximum CPU load at any time: " + str(find_max_cpu_load([Job(1, 4, 3), Job(2, 5, 4), Job(7, 9, 6)])))
    print("Maximum CPU load at any time: " + str(find_max_cpu_load([Job(6, 7, 10), Job(2, 4, 11), Job(8, 12, 15)])))
    print("Maximum CPU load at any time: " + str(find_max_cpu_load([Job(1, 4, 2), Job(2, 4, 1), Job(3, 6, 5)])))


main()
