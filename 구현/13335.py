#트럭
import sys
n, w, l = map(int, sys.stdin.readline().split())
truck = list(map(int, sys.stdin.readline().split()))
bridge = [0 for _ in range(w)]
cnt = 0 # cnt번쨰 트럭
time = 0 #최종 걸리는 시간

for i in truck:
    okay = 0
    zero_count = 0
    while okay != 1:
        if sum(bridge)+i < l:
            bridge.pop(0)
            bridge.append(i)
            time += 1
            okay = 1 #해당 트럭이 다리에 올라갔을 때 1
            cnt += 1
            print(bridge)

        else:
            zero_count += 1 
            bridge.pop(0)
            bridge.append(0)
            time += 1
            print(bridge)
    if cnt == n:
        time += w 

time = time - zero_count
print(time)
