import sys

def insert_path(root, path):
    current = root
    for part in path:
        if part not in current:
            current[part] = {}
        current = current[part]

def print_trie(trie, depth=0):
    for key in sorted(trie.keys()):
        print("--" * depth + key)
        print_trie(trie[key], depth + 1)

n = int(sys.stdin.readline())
root = {}

for _ in range(n):
    path = input().split()
    insert_path(root, path[1:])

print_trie(root)
