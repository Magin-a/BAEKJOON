#크리스마스 선물
import sys

import heapq
n = int(sys.stdin.readline())

gift= []
for _ in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    
    if a[0]== 0:
        if len(gift) == 0:
            print(-1)

        else:
            print(heapq.heappop(gift)[1])
    
    else:
        for i in range(1,a[0]+1):
            heapq.heappush(gift, (-a[i], a[i]))
