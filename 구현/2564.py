#경비원
import sys
from collections import deque
length, width = map(int, sys.stdin.readline().split()) # 직사각형 입력
n = int(sys.stdin.readline()) #상점가 갯수 입력

result = 0 # 최단경로 결과값
store = deque()
for _ in range(n+1):  #상점가와 경비 위치 값 입력
    x, y = map(int, sys.stdin.readline().split()) #x는 동서남북 값, y는 그외 위치값
    #조건문은 동서남북 위치 값을 행렬값으로 변환 과정
    if x  == 1: #
        store.append([0,y])

    elif x == 2:
        store.append([width, y])
    
    elif x == 3:
        store.append([y, 0])

    elif x == 4:
        store.append([y, length])

pol_x, pol_y = store.pop() # 맨마지막 값은 경비 위치 값



while store: #상점가 최소거리 
    test_x, test_y = store.popleft()
    
    if pol_x == 0 or pol_x == width: #경비 위치가 북 or 남
        if pol_x == test_x:
            result += abs(pol_y - test_y)

        elif abs(pol_x - test_x) == width: #경비와 상점가 위치가 같을 때
            result += width + min(pol_y+ test_y, (length-pol_y) + (length-test_y))

        else: #상점가 위치가 서 or 동 일 때
            result += abs(pol_x-test_x) +abs(pol_y-test_y)


    elif pol_y == 0 or pol_y == length: #경비 위치가 서 or 동
        if pol_y == test_y:
            result += abs(pol_x - test_x)

        elif abs(pol_y - test_y) == length: #경비와 상점가 위치가 같을 때
            result += length + min(pol_x+ test_x, (width-pol_x) + (width-test_x))

        else: #상점가 위치가 북 or 남 일 때
            result += abs(pol_x-test_x) +abs(pol_y-test_y)

print(result) 
