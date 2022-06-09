class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path(root, target):
    def pre_order_dfs(node, path=0):
        if not node:
            return False
        elif not node.left and not node.right:
            return path + node.val == target
        else:
            return any([pre_order_dfs(node.left, path + node.val),
                        pre_order_dfs(node.right, path + node.val)])

    return pre_order_dfs(root)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(has_path(root, 23)))
    print("Tree has path: " + str(has_path(root, 16)))


main()
