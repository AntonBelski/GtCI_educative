from heapq import heapify, heappop, heappush


def find_Kth_smallest(lists, k):
    filter_lists = [l for l in lists if l]
    heap = [[l[0], i, 0] for i, l in enumerate(filter_lists)]
    result = []
    heapify(heap)

    while len(result) != k:
        val, l_ind, ind = heappop(heap)
        result.append(val)
        if ind + 1 < len(filter_lists[l_ind]):
            ind += 1
            heappush(heap, [filter_lists[l_ind][ind], l_ind, ind])

    return result[-1] if filter_lists else None


def main():
    print("Kth smallest number is: " + str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))


main()
