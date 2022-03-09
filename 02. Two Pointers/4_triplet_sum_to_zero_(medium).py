def twoSum(first, curr_num, result):
    l = 0
    r = len(curr_num) - 1

    while r > l:
        if first + curr_num[l] + curr_num[r] > 0:
            r -= 1
        elif first + curr_num[l] + curr_num[r] < 0:
            l += 1
        else:
            result.add((first, curr_num[l], curr_num[r]))
            l += 1


def search_triplets(nums):
    if len(nums) < 3:
        return []

    nums.sort()
    result = set()

    for i in range(len(nums) - 2):
        twoSum(first=nums[i], curr_num=nums[i + 1:], result=result)

    return [list(s) for s in result]


def main():
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
    print(search_triplets([-5, 2, -1, -2, 3]))


main()
