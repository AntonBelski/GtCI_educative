def find_closest_elements(arr, k, x):
    start = 0
    end = len(arr) - 1

    while end + 1 - start != k:
        if abs(x - arr[start]) > abs(x - arr[end]):
            start += 1
        else:
            end -= 1

    return arr[start:end + 1]


def main():
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


main()
