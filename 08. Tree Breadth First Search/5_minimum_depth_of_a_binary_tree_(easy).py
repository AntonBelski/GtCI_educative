from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_minimum_depth(root):
    max_depth = float('inf')
    deq = deque()
    if root:
        deq.append([root, 1])
    else:
        return 0

    while deq:
        node, level = deq.popleft()
        if node.left:
            deq.append([node.left, level + 1])
        if node.right:
            deq.append([node.right, level + 1])
        if not node.left and not node.right:
            max_depth = min(max_depth, level)

    return max_depth


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()
