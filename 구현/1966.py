#프린터 큐
import sys
from collections import deque
test_num = int(sys.stdin.readline()) #테스트 갯수

def solution(file, wanted, site): #원하는 프린터 순서 찾는 함수
    x = deque() #
    
    for i in range(file):
        x.append([site[i], i])  #[중요도, index]
    
    cnt = 0 #프린트 순서
    while True:
        if x[0][0] == max(x)[0]: #처음꺼가 중요도가 가장 큰 수인가
            cnt += 1

            if x[0][1] == wanted: #내가 원하는 값이 맞는가?
                break
            
            x.popleft()
        else:
            x.append(x.popleft())# 처음꺼가 중요도가 가장 큰값이 아니라면 뒤로 보냄
    
    print(cnt) #최종 원하는 프린터 순서 출력
    

for _ in range(test_num):
    n, m = map(int,sys.stdin.readline().split())
    imp = list(map(int, sys.stdin.readline().split()))
    solution(n, m, imp)
    
