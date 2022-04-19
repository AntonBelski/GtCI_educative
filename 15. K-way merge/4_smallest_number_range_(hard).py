from heapq import heappop, heappush


def find_smallest_range(nums):
    heap = []
    high = -float('inf')
    for i in range(len(nums)):
        heappush(heap, [nums[i][0], i, 0])
        high = max(high, nums[i][0])
    result = [heap[0][0], high]

    while True:
        val, nums_i, i = heappop(heap)
        if i + 1 == len(nums[nums_i]):
            break
        new_val = nums[nums_i][i + 1]
        heappush(heap, [new_val, nums_i, i + 1])
        high = max(high, new_val)
        if high - heap[0][0] < result[1] - result[0]:
            result = [heap[0][0], high]

    return result


def main():
    print("Smallest range is: " +
          str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))


main()
