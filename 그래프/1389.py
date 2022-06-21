#케빈 베이컨의 6단계 법칙
#그래프, 플로이드-워셜(한지점에서 모든지점까지 최단 경로 구하기)
import sys
input = sys.stdin.readline
inf = int(1e9)
p = 1000000000

n, link_cnt = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]


for _ in range(link_cnt):
    start, fin = map(int, input().split())
    graph[start][fin] = 1
    graph[fin][start] = 1


#플로이드-워셜
for k in range(1, n+1):
    for x in range(1,n+1):
        for y in range(1, n+1):
            
            if x == y:
                continue

            elif graph[x][k] and graph[k][y]:

                if graph[x][y] == 0:
                    graph[x][y] = graph[x][k] + graph[k][y]

                else:
                    graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])

# 모든 시작점 탐색후 가장 작은 시작점 출력
for i in range(1,n+1):
    result = 0

    for j in range(1,n+1):
        result += graph[i][j]

    if p > result:
        p = result
        now = i

print(now)