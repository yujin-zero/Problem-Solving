import sys
sys.setrecursionlimit(10**6)

def find_tree(start_index, end_index, parent_node, left_or_right) :
    global root_index
    
    # print("start : " , start_index, "end : ", end_index, "parent_node : ",parent_node, "? : ", left_or_right)
    
    root_node = post_order[root_index]

    parent[root_node] = parent_node
    if left_or_right == 'L' :
        left_child[parent_node] = root_node
    else :
        right_child[parent_node] = root_node

    in_root_index = node_index[root_node]

    # 오른쪽으로 보내기
    if end_index > in_root_index :
        root_index -= 1
        find_tree(in_root_index+1, end_index, root_node, 'R')

     # 왼쪽으로 보내기
    if start_index < in_root_index :
        root_index -= 1
        find_tree(start_index, in_root_index-1,root_node, 'L')


def pre_order(root) :
    print(root,end=' ')
    if left_child[root] != -1 :
        pre_order(left_child[root])
    if right_child[root] != -1 :
        pre_order(right_child[root])

n = int(sys.stdin.readline())
in_order = list(map(int,sys.stdin.readline().split()))
post_order = list(map(int,sys.stdin.readline().split()))
left_child = [-1] * (n+1) # 왼쪽 자식
right_child = [-1] * (n+1) # 오른쪽 자식
parent = [-1] * (n+1) # 부모
node_index = [-1] * (n+1)
for i in range(n) :
    value = in_order[i]
    node_index[value] = i

root_index = n-1
find_tree(0,n-1,0,'L')

# 전위순회 출력
pre_order(post_order[-1])