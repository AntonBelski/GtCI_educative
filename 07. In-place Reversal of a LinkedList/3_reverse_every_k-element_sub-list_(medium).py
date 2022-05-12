from __future__ import print_function


class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse_every_k_elements(head, k):
    if not head.next or k == 1:
        return head

    list_len = 1
    node = head
    while node.next:
        node = node.next
        list_len += 1

    pre_head = Node(next=head)
    result_head = None
    start = 0
    while start + 2 <= list_len:
        prev_node = None
        node = pre_head.next
        next_node = node.next
        node.next = prev_node
        start += 1

        for i in range(k - 1):
            prev_node = node
            node = next_node
            next_node = node.next
            node.next = prev_node
            start += 1

            if start == list_len:
                break

        pre_head.next.next = next_node
        new_head = pre_head.next
        pre_head.next = node
        pre_head = new_head

        if not result_head:
            result_head = node

    return result_head if result_head else head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_every_k_elements(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
