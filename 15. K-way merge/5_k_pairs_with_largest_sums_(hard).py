from heapq import heapify, heappush, heappop


def find_k_largest_pairs(nums1, nums2, k):
    result = []
    heap = []
    for i, val in enumerate(nums2):
        heap.append([nums1[0] + val, i, 0])
    heapify(heap)

    while heap and k:
        val, n2_i, n1_i = heappop(heap)
        if n1_i + 1 < len(nums1):
            new_val = nums1[n1_i + 1] + nums2[n2_i]
            heappush(heap, [new_val, n2_i, n1_i + 1])
        result.append([nums1[n1_i], nums2[n2_i]])
        k -= 1

    return result


def main():
    print("Pairs with largest sum are: " +
          str(find_k_largest_pairs([9, 8, 2], [6, 3, 1], 3)))


main()
