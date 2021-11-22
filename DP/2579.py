import sys

n = int(sys.stdin.readline())
stair = []

for _ in range(n):
    stair.append(int(sys.stdin.readline()))

d = [0]*n
d[0] = stair[0]

if n <3:
    d[n-1] = sum(stair)

else:
    for x in range(1,n):
        if x == 1:
            d[x] = max(stair[x]+d[x-1], stair[x-1])
            continue
        d[x] = max(stair[x]+stair[x-1], stair[x]+d[x-2])

    for i in range(3, n):
        d[i] = max(stair[i]+stair[i-1]+ d[i-3], stair[i]+d[i-2])
print(d[-1])
