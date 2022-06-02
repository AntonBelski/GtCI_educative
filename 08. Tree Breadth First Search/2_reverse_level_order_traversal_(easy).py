from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    deq = deque()
    if root:
        deq.append([root, 0])
    while deq:
        node, level = deq.popleft()
        if level == len(result):
            result.append([])
        result[level].append(node.val)
        if node.left:
            deq.append([node.left, level + 1])
        if node.right:
            deq.append([node.right, level + 1])

    return result[::-1]


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " + str(traverse(root)))


main()
