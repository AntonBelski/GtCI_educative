class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_numbers(root):
    def dfs(node, path=0):
        if not node:
            return 0
        curr_path = path * 10 + node.val
        if not node.left and not node.right:
            return curr_path
        return dfs(node.left, curr_path) + dfs(node.right, curr_path)

    return dfs(root)


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
