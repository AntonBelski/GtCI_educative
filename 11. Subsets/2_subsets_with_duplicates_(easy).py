def recursive_subsets(nums, result, subset=[], index=0):
    for i in range(index, len(nums)):
        if i != index and nums[i] == nums[i - 1]:
            continue
        subset.append(nums[i])
        result.append(subset[:])
        recursive_subsets(nums, result, subset, i + 1)
        subset.pop()


def find_subsets(nums):
    nums.sort()
    result = [[]]
    recursive_subsets(nums, result)
    return result


def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()
