from collections import Counter


def find_maximum_distinct_elements(nums, k):
    nums_counter = Counter(nums)
    freq_counter = Counter(nums_counter.values())
    result = freq_counter[1]

    for freq in range(2, len(nums) + 1):
        if k == 0:
            return result
        elif freq_counter[freq] * (freq - 1) <= k:
            k -= freq_counter[freq] * (freq - 1)
            result += freq_counter[freq]
        else:
            return result + k // (freq - 1)

    return result - k


def main():
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))


main()
