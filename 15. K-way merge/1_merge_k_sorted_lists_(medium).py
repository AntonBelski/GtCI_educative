from __future__ import print_function
from heapq import heapify, heappop, heappush


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def merge_lists(lists):
    filter_lists = [l for l in lists if l]
    heap = [[l.value, i] for i, l in enumerate(filter_lists)]
    result = []

    heapify(heap)
    while heap:
        val, ind = heappop(heap)

        if filter_lists[ind].next:
            next_node = filter_lists[ind].next
            heappush(heap, [next_node.value, ind])
            filter_lists[ind] = next_node

        new_node = ListNode(val)
        result.append(new_node)
        if len(result) != 1:
            result[-2].next = result[-1]

    return result[0] if filter_lists else None


def main():
    l1 = ListNode(2)
    l1.next = ListNode(6)
    l1.next.next = ListNode(8)

    l2 = ListNode(3)
    l2.next = ListNode(6)
    l2.next.next = ListNode(7)

    l3 = ListNode(1)
    l3.next = ListNode(3)
    l3.next.next = ListNode(4)

    result = merge_lists([l1, l2, l3])
    print("Here are the elements form the merged list: ", end='')
    while result:
        print(str(result.value) + " ", end='')
        result = result.next


main()
