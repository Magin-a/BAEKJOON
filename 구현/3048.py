#개미
import sys
input = sys.stdin.readline

g1_cnt, g2_cnt = map(int, input().split())
g1 = list(reversed(input().rstrip())) #진행방향에 맞게 reverse
g2 = list(input().rstrip())
time = int(input())

result = g1 + g2

num = 0

#시간 기준 
while num < time:
    #해당 시간초에 개미들의 변화
    for i in result[:-1]: # 마지막 값은 result[-2]값 순서에서 처리함
        x = result.index(i)
        if i in g1: #순서를 뒤집는데 기준이 되는 g1
            if result[x+1] in g2: 
                result[x], result[x+1] = result[x+1], result[x]

            else:
                continue

        else:
            continue
    num += 1 #다음 시간

for p in result: #출력
    print(p, end='')
