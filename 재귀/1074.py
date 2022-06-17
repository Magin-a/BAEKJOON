#Z
#분할 정복, 재귀
import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

result =0

while n != 0:
    n -= 1

    #목표값이 있는 구역 찾기
    if r < 2**n and c < 2**n: #1사분면
        result += (2**n * 2**n)*0 

    elif r < 2**n and c >= 2**n: #2사분면
        result += (2**n * 2**n)*1
        c -= 2**n #목표값이 있는 사분면으로 범위 조정

    elif r >= 2**n and c < 2**n: # 3사분면
        result += (2**n * 2**n)*2 
        r -= 2**n #목표값이 있는 사분면으로 범위 조정

    elif r >= 2**n and c >= 2**n: #4사분면
        result += (2**n * 2**n)*3 
        r -= 2**n #목표값이 있는 사분면으로 범위 조정
        c -= 2**n #목표값이 있는 사분면으로 범위 조정

print(result)