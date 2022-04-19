from heapq import heapify, heappop, heappush


def find_maximum_capital(capital, profits, k, w):
    max_heap, min_heap = [], []
    max_capital = w

    for i in range(len(profits)):
        min_heap.append([capital[i], profits[i]])

    heapify(min_heap)
    for _ in range(k):
        while min_heap and min_heap[0][0] <= max_capital:
            heappush(max_heap, -heappop(min_heap)[1])

        if not max_heap:
            break

        max_capital += -heappop(max_heap)

    return max_capital


def main():
    print("Maximum capital: " +
          str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
    print("Maximum capital: " +
          str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))


main()
