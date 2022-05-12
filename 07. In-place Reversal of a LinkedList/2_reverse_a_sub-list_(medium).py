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


def reverse_sub_list(head, left, right):
    pre_left = Node(next=head)
    count = 1
    while count != left:
        pre_left = pre_left.next
        count += 1

    prev_node = None
    node = pre_left.next
    next_node = node.next
    node.next = prev_node
    count += 1

    while count <= right:
        prev_node = node
        node = next_node
        next_node = node.next
        node.next = prev_node
        count += 1

    pre_left.next.next = next_node
    pre_left.next = node

    return pre_left.next if left == 1 else head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_sub_list(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
