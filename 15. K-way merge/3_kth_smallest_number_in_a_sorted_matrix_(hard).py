from heapq import heapify, heappop, heappush


def find_Kth_smallest(matrix, k):
    max_len = len(matrix)
    heap = [[row[0], ind, 0] for ind, row in enumerate(matrix)]
    heapify(heap)

    while k:
        k -= 1
        val, matr_ind, row_ind = heappop(heap)

        if row_ind + 1 < max_len:
            new_val = matrix[matr_ind][row_ind + 1]
            heappush(heap, [new_val, matr_ind, row_ind + 1])

    return val


def main():
    print("Kth smallest number is: " +
          str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))


main()
