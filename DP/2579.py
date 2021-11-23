#계단오르기
import sys

n = int(sys.stdin.readline()) #계단 갯수
stair = [] #계단 저장

for _ in range(n): #N개만큼 계단 생성
    stair.append(int(sys.stdin.readline()))

d = [0]*n #계단 갯수만큼 확보
d[0] = stair[0]

if n <3: #계단의 갯수가 3개미만일때
    d[n-1] = sum(stair)

else:
    for x in range(1,3):
        if x == 1: #두번째 계단
            d[x] = max(stair[x]+d[x-1], stair[x-1]) #두번째 계단까지 올라가는 최고의 값
            continue
        d[x] = max(stair[x]+stair[x-1], stair[x]+d[x-2])#3번째 계단까지 올라가는 최고의 값

    for i in range(3, n): #4번째계단부터
        d[i] = max(stair[i]+stair[i-1]+ d[i-3], stair[i]+d[i-2]) #i+1번째 계단까지 가는 최댓값

print(d[-1])
