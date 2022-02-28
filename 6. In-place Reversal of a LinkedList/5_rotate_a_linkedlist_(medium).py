from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def rotate(head, k):
    if not head or not head.next:
        return head

    list_len = 1
    tail = head

    while tail.next:
        tail = tail.next
        list_len += 1

    if not k % list_len:
        return head

    end = list_len - k % list_len
    start = 1
    node = head

    while start != end:
        node = node.next
        start += 1

    new_head = node.next
    node.next = None
    tail.next = head

    return new_head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = rotate(head, 3)
    print("Nodes of rotated LinkedList are: ", end='')
    result.print_list()


main()
