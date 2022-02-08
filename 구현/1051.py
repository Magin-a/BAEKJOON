#숫자 정사각형
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

graph = [list(map(int, input().rstrip())) for _ in range(n)]

def angle():
    result = 1
    for idx, a in enumerate(graph):
        find_num = deque()
        for b in a:
            if b not in find_num and a.count(b) >= 2:
                find_num.append(b)
            continue
        while find_num:
            test = find_num.popleft()
            num_x1, num_x2 = a.index(test), a.index(test, a.index(test)+1)
            w = num_x2 - num_x1
            
            if idx+w <n and test == graph[idx+w][num_x1] and test == graph[idx+w][num_x2]:
                result = max(result, (w+1)**2)
            
    return result

a = angle()
print(a)

#완료
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
g = [list(map(int, input().rstrip())) for _ in range(n)]


check = min(n, m)
answer = 0
for i in range(n):
    for j in range(m):
        for k in range(check):
            if ((i + k) < n) and ((j + k) < m) and (g[i][j] == g[i][j + k] == g[i + k][j] == g[i + k][j + k]): #같은 숫자 정사각형 확인
                answer = max(answer, (k + 1)**2)
                
print(answer)
