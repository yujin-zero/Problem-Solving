import sys
sys.setrecursionlimit(10**6)


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def construct_tree(preorder, start, end):
    if start > end:
        return None

    root = TreeNode(preorder[start])
    i = start + 1
    while i <= end:
        if preorder[i] > root.val:
            break
        i += 1

    root.left = construct_tree(preorder, start+1, i-1)
    root.right = construct_tree(preorder, i, end)
    return root


def rearorder(root):
    if root:
        rearorder(root.left)
        rearorder(root.right)
        print(root.val)


x = sys.stdin.readline()
preorder = []
while x:
    preorder.append(int(x))
    x = sys.stdin.readline().rstrip()

root = construct_tree(preorder, 0, len(preorder)-1)
rearorder(root)
