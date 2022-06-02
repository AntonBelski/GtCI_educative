from __future__ import print_function
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def tree_right_view(root):
    deq = deque()
    result = []
    if root:
        deq.append([root, 0])

    while deq:
        node, level = deq.popleft()
        if node.left:
            deq.append([node.left, level + 1])
        if node.right:
            deq.append([node.right, level + 1])
        if deq and level != deq[0][1]:
            result.append(node)
    if root:
        result.append(node)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = tree_right_view(root)
    print("Tree right view: ")
    for node in result:
        print(str(node.val) + " ", end='')


main()
