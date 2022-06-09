class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path(root, arr):
    def dfs(node, depth=0):
        if not node or depth == len(arr) or arr[depth] != node.val:
            return False
        if not node.left and not node.right and depth + 1 == len(arr):
            return True
        return any([dfs(node.left, depth + 1),
                    dfs(node.right, depth + 1)])

    return dfs(root)


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
