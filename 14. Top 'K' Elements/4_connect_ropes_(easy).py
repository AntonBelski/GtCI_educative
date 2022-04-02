from heapq import heapify, heappop, heappush


def minimum_cost_to_connect_ropes(sticks):
    result = 0
    heapify(sticks)

    while len(sticks) > 1:
        first_min = heappop(sticks)
        second_min = heappop(sticks)
        result += first_min + second_min
        heappush(sticks, first_min + second_min)

    return result


def main():
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))


main()
