from collections import Counter
from heapq import heapify, heappop, heappush


def reorganize_string(s, k):
    s_counter = Counter(s)
    window = {}
    result = []

    if len(s_counter) < k:
        return ''
    elif k < 2:
        return s

    heap = [[-freq, ch] for ch, freq in s_counter.items()]
    heapify(heap)

    for _ in range(k):
        freq, ch = heappop(heap)
        result.append(ch)
        window[ch] = freq + 1

    for i in range(k, len(s)):
        ch = result[i - k]
        freq = window.pop(ch)
        if freq != 0:
            heappush(heap, [freq, ch])

        if not heap:
            return ''

        freq, ch = heappop(heap)
        result.append(ch)
        window[ch] = freq + 1

    return ''.join(result)


def main():
    print("Reorganized string: " + reorganize_string("mmpp", 2))
    print("Reorganized string: " + reorganize_string("Programming", 3))
    print("Reorganized string: " + reorganize_string("aab", 2))
    print("Reorganized string: " + reorganize_string("aapa", 3))


main()
