from collections import Counter
from heapq import heapify, heappop


def sort_character_by_frequency(s):
    result = []
    s_freq = Counter(s)

    freq_pairs = [(-freq, ch) for ch, freq in s_freq.items()]
    heapify(freq_pairs)

    while freq_pairs:
        freq, ch = heappop(freq_pairs)
        result.append(-freq * ch)

    return ''.join(result)


def main():
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("Programming"))
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("abcbab"))


main()
