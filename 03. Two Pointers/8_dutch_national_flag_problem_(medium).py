def dutch_flag_sort(nums):
    last_not_zero = 0
    last_not_two = len(nums) - 1
    i = 0

    while i <= last_not_two:
        if nums[i] == 2:
            nums[i], nums[last_not_two] = nums[last_not_two], nums[i]
            last_not_two -= 1
        elif nums[i] == 0:
            nums[i], nums[last_not_zero] = nums[last_not_zero], nums[i]
            last_not_zero += 1
            i += 1
        else:
            i += 1


def main():
    arr = [1, 0, 2, 1, 0]
    dutch_flag_sort(arr)
    print(arr)

    arr = [2, 2, 0, 1, 2, 0]
    dutch_flag_sort(arr)
    print(arr)


main()
