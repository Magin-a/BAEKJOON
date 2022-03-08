#1, 2, 3 더하기 3
import sys
input = sys.stdin.readline

goals = [1, 2, 4, 7] #1, 2, 4, 7, 13, 24, 44 ~

for _ in range(int(input())): #테스트 갯수
    n = int(input())
    for i in range(len(goals), n):
        goals.append((goals[i-3] + goals[i-2] + goals[i-1])%1000000009)  #점화식
    print(goals[n-1])