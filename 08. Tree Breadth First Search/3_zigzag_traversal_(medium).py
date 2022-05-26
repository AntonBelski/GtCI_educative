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

    for i in range(len(result)):
        if i % 2 == 1:
            result[i].reverse()

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse(root)))


main()
