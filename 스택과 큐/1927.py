#최소 힙
#자료구조, 우선순위 큐
import sys
import heapq
input = sys.stdin.readline
q = []
n = int(input())

for _ in range(n):
    num = int(input())
    if num == 0: #입력 숫자가 0일때 배열안에 최소 수 출력
        if q:
            print(heapq.heappop(q))
        
        else: #입력 숫자가 0인데 배열에 값이 없다면
            print(0)

    else:#배열 추가
        heapq.heappush(q, num)

