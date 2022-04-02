from heapq import heappush, heappop, heappushpop


class KthLargestNumberInStream:
    def __init__(self, nums, k):
        self.heap = []
        self.k = k
        for elem in nums:
            if len(self.heap) < k:
                heappush(self.heap, elem)
            else:
                heappushpop(self.heap, elem)

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        if len(self.heap) > self.k:
            heappop(self.heap)
        return self.heap[0]


def main():
    kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
    print("4th largest number is: " + str(kthLargestNumber.add(6)))
    print("4th largest number is: " + str(kthLargestNumber.add(13)))
    print("4th largest number is: " + str(kthLargestNumber.add(4)))


main()
