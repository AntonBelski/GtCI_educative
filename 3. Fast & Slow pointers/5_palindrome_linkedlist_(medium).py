class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def is_palindromic_linked_list(head):
    if not head.next:
        return True

    slow = head
    fast = head
    is_palindrome = True

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    last_node = reverse_list(slow)
    start_node = head
    end_node = last_node

    while end_node:
        if start_node.value != end_node.value:
            is_palindrome = False
            break
        start_node = start_node.next
        end_node = end_node.next

    reverse_list(last_node)
    return is_palindrome


def reverse_list(node):
    prev_node = None
    next_node = node.next
    node.next = prev_node

    while next_node:
        prev_node = node
        node = next_node
        next_node = node.next
        node.next = prev_node

    return node


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome: " + str(is_palindromic_linked_list(head)))

    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()
