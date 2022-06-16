import math


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_maximum_path_sum(root):
    def dfs(node, result):
        if not node:
            return 0
        left_max = max(dfs(node.left, result), 0)
        right_max = max(dfs(node.right, result), 0)
        result[0] = max(result[0], left_max + right_max + node.val)
        return node.val + max(left_max, right_max)

    result = [-float('inf')]
    dfs(root, result)
    return result[0]


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))

    root = TreeNode(-1)
    root.left = TreeNode(-3)
    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))


main()
