def find_single_numbers(nums):
    all_xor = 0

    for num in nums:
        all_xor ^= num

    rightmost_bit = all_xor & (-all_xor)
    x = 0

    for num in nums:
        if num & rightmost_bit:
            x ^= num

    y = all_xor ^ x
    return [x, y]


def main():
    print('Single numbers are:' +
          str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
    print('Single numbers are:' + str(find_single_numbers([2, 1, 3, 2])))


main()
