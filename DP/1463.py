#1로 만들기
import sys
input = sys.stdin.readline

n = int(input())


d = [0]*(n+1)

for i in range(2, n+1):
    d[i] = d[i-1] + 1 #일반적인 1씩 뺴기 했을시 카운트

    if i % 2 == 0: #2로 나누어 떨어질때
        d[i] = min(d[i], d[i//2]+1)
        

    if i % 3 == 0: #3으로 나누어 떨어질 때
        d[i] = min(d[i], d[i//3]+1)
        
print(d[n]) # n이 1일 될꺠까지  나누어야 할 횟수 카운트