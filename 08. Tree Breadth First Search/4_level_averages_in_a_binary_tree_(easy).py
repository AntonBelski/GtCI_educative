from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_level_averages(root):
    result = []
    prev_level = -1
    deq = deque()
    deq.append([root, 0])

    while deq:
        node, level = deq.popleft()
        if level != prev_level:
            if prev_level >= 0:
                result.append(level_sum / count)
            level_sum, count = node.val, 1
        else:
            level_sum += node.val
            count += 1
        prev_level = level

        if node.left:
            deq.append([node.left, level + 1])
        if node.right:
            deq.append([node.right, level + 1])

    result.append(level_sum / count)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level averages are: " + str(find_level_averages(root)))


main()
