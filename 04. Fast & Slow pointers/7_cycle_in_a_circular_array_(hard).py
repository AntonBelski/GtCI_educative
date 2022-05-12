def circular_array_loop_exists(nums):
    n = len(nums)
    for i in range(n):
        if nums[i] == 0:
            continue

        slow = fast = (nums[i] + i) % n
        fast = (nums[fast] + fast) % n

        while slow != fast:
            slow = (nums[slow] + slow) % n
            fast = (nums[fast] + fast) % n
            fast = (nums[fast] + fast) % n

        next_slow = (nums[slow] + slow) % n
        if slow != next_slow:
            while next_slow != fast:
                if not ((nums[slow] > 0) == (nums[next_slow] > 0)):
                    break
                slow = next_slow
                next_slow = (nums[next_slow] + next_slow) % n
            else:
                return True

        next_ind = i
        while nums[next_ind] != 0:
            nums[next_ind], next_ind = 0, (nums[next_ind] + next_ind) % n
    return False


def main():
    print(circular_array_loop_exists([1, 2, -1, 2, 2]))
    print(circular_array_loop_exists([2, 2, -1, 2]))
    print(circular_array_loop_exists([2, 1, -1, -2]))


main()
