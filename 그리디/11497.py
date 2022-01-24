#통나무 건너뛰기

#수 비교의 구현
import sys
from collections import deque
input = sys.stdin.readline

test = int(input())

for _ in range(test):
    num_cnt = int(input())
    num = list(sorted(map(int, input().split())))
    result= deque()
    while num:
        if not result:
            n = num.pop()
            result.append(n)
            level = 0

        a = num.pop()
        if not num:
            result.appendleft(a)
            break
        result.appendleft(a)
        level = max(result[1]-a, level)

        b = num.pop()
        result.append(b)
        level = max(result[-2]-b, level)

    print(level)


#2안
import sys
from collections import deque
input = sys.stdin.readline

test = int(input())

for _ in range(test): #해당 test의 입력
    num_cnt = int(input())
    num = list(sorted(map(int, input().split())))
    result = 0

    #현재의 수와 건너뛴 수만의 비교로 result 값 갱신
    for i in range(2,num_cnt-2): 
        result = max(num[i]-num[i-2], num[i+2]-num[i], result) # 1번 i-(i-2)  2번 (i+2)-i 3번  기존 result 비교 갱신
    print(result)
