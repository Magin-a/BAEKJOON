#크리스마스 선물
import sys
import heapq
n = int(sys.stdin.readline())#입력 횟수 

gift= [] #선물 저장
for _ in range(n):
    a = list(map(int, sys.stdin.readline().split()))# 아이들 or 거점 이동
    
    if a[0]== 0: #아이들과 만남
        if len(gift) == 0: #줄 선물이 없다
            print(-1)

        else:#줄 선물이 있다
            print(heapq.heappop(gift)[1])
    
    else: #거점지 선물 충전
        for i in range(1,a[0]+1): 
            heapq.heappush(gift, (-a[i], a[i])) # (-a[i], a[i]) 앞에 '-' 추가함으로 큰수기준으로 정렬
