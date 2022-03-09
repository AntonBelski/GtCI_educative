from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
        print()

def get_cycle_len(slow):
    cycle_len = 1
    cycle_pointer = slow.next

    while cycle_pointer != slow:
        cycle_pointer = cycle_pointer.next
        cycle_len += 1

    return cycle_len


def find_cycle_start(head):
    if not head:
        return None

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            cycle_len = get_cycle_len(slow)
            head_ahead = head

            for i in range(cycle_len):
                head_ahead = head_ahead.next

            while head != head_ahead:
                head = head.next
                head_ahead = head_ahead.next

            return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()
