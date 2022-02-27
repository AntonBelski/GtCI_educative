def find_first_k_missing_positive(nums, k):
    result = []
    uniq_nums = set(nums)
    integer = 1

    while len(result) < k:
        if integer not in uniq_nums:
            result.append(integer)
        integer += 1

    return result


def main():
    print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
    print(find_first_k_missing_positive([2, 3, 4], 3))
    print(find_first_k_missing_positive([-2, -3, 4], 2))


main()
