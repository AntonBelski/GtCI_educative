class ArrayReader:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return float('inf')
        return self.arr[index]


def search_in_infinite_array(reader, x):
    lo, hi = 0, 10000
    while lo != hi:
        mid = (lo + hi) // 2
        if x <= reader.get(mid):
            hi = mid
        else:
            lo = mid + 1

    if reader.get(lo) == x:
        return lo
    else:
        return -1


def main():
    reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    print(search_in_infinite_array(reader, 16))
    print(search_in_infinite_array(reader, 11))
    reader = ArrayReader([1, 3, 8, 10, 15])
    print(search_in_infinite_array(reader, 15))
    print(search_in_infinite_array(reader, 200))


main()
