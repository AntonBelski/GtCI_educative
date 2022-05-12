def make_squares(nums):
    l = 0
    r = len(nums) - 1
    result = []

    while r >= l:
        if nums[r] ** 2 > nums[l] ** 2:
            result.append(nums[r] ** 2)
            r -= 1
        else:
            result.append(nums[l] ** 2)
            l += 1

    return result[::-1]


def main():
    print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
    print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()
