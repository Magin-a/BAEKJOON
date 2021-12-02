#이진트리 검색
import sys
sys.setrecursionlimit(10**9)

def tree(start, end):
    if start > end:
        return

    root = preder[start]
    find = start +1
    while find <= end:
        if root < preder[find]:
            break
        find += 1
    
    tree(start+1,find-1)
    tree(find, end)
    print(root)

preder = []
while True:
    try:
        preder.append(int(sys.stdin.readline()))

    except:
        break


tree(0, len(preder)-1)
