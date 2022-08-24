import sys
input = sys.stdin.readline

n, m = map(int, input().split())
friend = [[] for _ in range(n)] #친분 관계
w = list(map(int, input().split())) # 무게(넘버순)
result = [] # 조건에 해당하는 사람들

for _ in range(m):
    ind, ring = map(int, input().split())
    friend[ind-1].append(ring-1)
    friend[ring-1].append(ind-1)

for inx, x in enumerate(friend):
    state = 0

    if len(x) == 0:
        result.append(inx)

    for idx, a in enumerate(x):
        if w[inx] > w[a]:
            if len(x) == (idx+1) and inx not in result:
                result.append(inx)

        else:
            state = 1
            break
    
    if state == 1:
        continue

print(len(result))