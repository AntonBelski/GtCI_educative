def recursive_subsets(nums, current_list, result, start=0):
    for i in range(start, len(nums)):
        current_list.append(nums[i])
        result.append(current_list[:])
        recursive_subsets(nums, current_list, result, i + 1)
        current_list.pop()
    return result


def find_subsets(nums):
    # Time Complexity - O(n * 2^n), Space Complexity - O(n), good proof of asymptotic in the notebook.
    result = [[]]
    current_list = []
    return recursive_subsets(nums, current_list, result)


def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()
