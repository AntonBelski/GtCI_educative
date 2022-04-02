from collections import Counter
from heapq import heappush, heappop


def find_k_frequent_numbers(nums, k):
    nums_freq = Counter(nums)
    result = []

    for num, freq in nums_freq.items():
        heappush(result, (freq, num))
        if len(result) > k:
            heappop(result)

    for i in range(len(result)):
        result[i] = result[i][1]

    return result


def main():
    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()
