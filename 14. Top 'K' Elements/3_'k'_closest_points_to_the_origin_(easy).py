from heapq import heappush, heappop


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')


def find_closest_points(points, k):
    result = []

    for ind, p in enumerate(points):
        dist = p.x ** 2 + p.y ** 2
        heappush(result, (-dist, ind))
        if len(result) > k:
            heappop(result)

    for i in range(len(result)):
        result[i] = points[result[i][1]]

    return result


def main():
    result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
    print("Here are the k points closest the origin: ", end='')
    for point in result:
        point.print_point()


main()
