def find_subarrays(nums, k):
    results = []
    l = 0
    product = 1

    for r in range(len(nums)):
        product *= nums[r]
        while product >= k and r >= l:
            product //= nums[l]
            l += 1

        if r >= l:
            for i in range(l, r + 1):
                results.append(nums[i:r + 1])

    return results


def main():
    print(find_subarrays([2, 5, 3, 10], 30))
    print(find_subarrays([8, 2, 6, 5], 50))


main()
