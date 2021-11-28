#1991(트리순회)
import sys

n = int(sys.stdin.readline())
tree = [[0]*3 for _ in range(26)]

for x in range(n):
    node, left, right = sys.stdin.readline().strip().split()
    tree[ord(node)-65] = [node,left,right]



def preder(node):
    print(node, end='')
    if tree[ord(node)-65][1] != '.':
        preder(tree[ord(node)-65][1])

    if tree[ord(node)-65][2] != '.':
        preder(tree[ord(node)-65][2])
    


def inorder(node):
    if tree[ord(node)-65][1] != '.':
        inorder(tree[ord(node)-65][1])
    print(node, end='')
    if tree[ord(node)-65][2] != '.':
        inorder(tree[ord(node)-65][2])

def postorder(node):
    if tree[ord(node)-65][1] != '.':
        postorder(tree[ord(node)-65][1])
    
    if tree[ord(node)-65][2] != '.':
        postorder(tree[ord(node)-65][2])
    print(node, end='')


preder('A')
print()
inorder('A')
print()
postorder('A')
