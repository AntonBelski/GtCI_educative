def backtracking(nums, result, current, first=0):
    if len(current) == len(nums):
        result.append(current[:])
        return
    for i in range(first, len(nums)):
        current.append(nums[i])
        nums[i], nums[first] = nums[first], nums[i]
        backtracking(nums, result, current, first + 1)
        nums[i], nums[first] = nums[first], nums[i]
        current.pop()


def find_permutations(nums):
    result, current = [], []
    backtracking(nums, result, current)
    return result


def main():
    print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()
