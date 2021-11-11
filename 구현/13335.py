import sys
from collections import deque

n, w, l = map(int, sys.stdin.readline().split())
truck = deque(list(map(int, sys.stdin.readline().split())))
bridge = deque(0 for _ in range(w))
count = 0  #최종 트럭이 다리를 건너는데 걸리는 시간

while truck: #트럭의 있는동안 반복
    bridge.popleft() #다리 위에 한칸씩 이동
    if sum(bridge) + truck[0] <= l: #다리의 최대무게가 넘지 않는다면 트럭 추가
        bridge.append(truck.popleft())
        count += 1 #이동시간 +1
    
    else: #다리의 최대 무게가 넘는다면 0추가
        bridge.append(0) 
        count += 1 

if sum(bridge) > 0: #다리 위에 트럭이 남아 있다면 다리를 건널 때까지pop
    while sum(bridge) != 0:
        bridge.popleft()
        count +=1
print(count) #최종 걸린시간
