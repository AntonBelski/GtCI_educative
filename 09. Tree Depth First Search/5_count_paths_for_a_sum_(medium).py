from collections import defaultdict


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_paths(root, target):
    def dfs(node, paths, path=0):
        if not node:
            return 0
        path += node.val
        result = paths[path - target]
        paths[path] += 1
        result += dfs(node.left, paths, path) + dfs(node.right, paths, path)
        paths[path] -= 1
        return result

    paths = defaultdict(int)
    paths[0] = 1
    return dfs(root, paths)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))


main()
