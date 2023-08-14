import sys


class TreeNode:
    def __init__(self, value, left_node, right_node):
        self.left = left_node
        self.right = right_node
        self.data = value


def preorder(node):
    if node:
        print(node.data, end='')
        if node.left:
            preorder(tree[node.left])
        if node.right:
            preorder(tree[node.right])


def inorder(node):
    if node:
        if node.left:
            inorder(tree[node.left])
        print(node.data, end='')
        if node.right:
            inorder(tree[node.right])


def rearorder(node):
    if node:
        if node.left:
            rearorder(tree[node.left])
        if node.right:
            rearorder(tree[node.right])
        print(node.data, end='')


n = int(sys.stdin.readline())
tree = {}

for _ in range(n):
    data, left, right = sys.stdin.readline().split()
    if left == '.':
        left = None
    if right == '.':
        right = None
    tree[data] = TreeNode(data, left, right)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
rearorder(tree['A'])
print()
