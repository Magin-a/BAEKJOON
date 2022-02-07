#도형정사각형
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
            num_x1, num_x2 = a.index(test), a.index(test, -1)
            # print('x',num_x1, num_x2)

            y1, y2 = 0, 0
            for _ in range(n-1):
                y1 += 1
                y2 += 1
                if graph[y1][num_x1] == test and graph[y2][num_x2] == test:
                    num_y2 = y2

                else:
                    continue
            
            if (y2-y1) != (num_x1):
                continue
        
        result = max(result, ((num_x2-num_x1)+1)*((num_y2-idx)+1))
            
        return result

a = angle()
print(a)
