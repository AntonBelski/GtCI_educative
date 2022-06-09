class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, target):
    result = []
    curr_path = []

    def dfs(node, path_sum=0):
        if not node:
            return
        curr_path.append(node.val)
        if not node.left and not node.right:
            if path_sum + node.val == target:
                result.append(curr_path[:])
        dfs(node.left, path_sum + node.val)
        dfs(node.right, path_sum + node.val)
        curr_path.pop()

    dfs(root)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) +
          ": " + str(find_paths(root, sum)))


main()
