#징검다리2
import sys
input = sys.stdin.readline

n = int(input())
brige = list(map(int, input().split()))

col = []

for i in range(n-1):
    a, b = brige[i], brige[i+1]
    col.append(a-b)
    
for j in col:
    if 