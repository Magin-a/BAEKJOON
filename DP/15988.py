#1, 2, 3 더하기 3
import sys
input = sys.stdin.readline

t = int(input())

goals = []

for _ in range(3):
    goals.append(int(input()))


goal= [0] * (max(goals)+1)
goal[0] = 1

for num in range(1, 4):
    for n in range(max(goals)+1):
        goal[n] += goal[n-num]

for x in goals:
    print(goal[x])
