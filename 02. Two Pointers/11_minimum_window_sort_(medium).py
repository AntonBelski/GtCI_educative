def shortest_window_sort(nums):
    min_l = float('inf')
    min_r = -float('inf')
    is_unsorted_exist = False

    for i in range(1, len(nums)):
        if nums[i - 1] > nums[i]:
            is_unsorted_exist = True
            min_l = min(min_l, nums[i])

    if is_unsorted_exist:
        for i in range(len(nums)):
            if nums[i] > min_l:
                min_l = i
                break

    for i in (range(len(nums) - 2, -1, -1)):
        if nums[i] > nums[i + 1]:
            is_unsorted_exist = True
            min_r = max(min_r, nums[i])

    if is_unsorted_exist:
        for i in (range(len(nums) - 1, -1, -1)):
            if nums[i] < min_r:
                min_r = i
                break

    return min_r + 1 - min_l if is_unsorted_exist else 0


def main():
    print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
    print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
    print(shortest_window_sort([1, 2, 3]))
    print(shortest_window_sort([3, 2, 1]))


main()
