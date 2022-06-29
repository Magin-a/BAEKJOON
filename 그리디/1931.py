#회의실 배정
#그리디
import sys
input = sys.stdin.readline

n = int(input())
time = []
for _ in range(n):
    start, fin = map(int, input().split())
    time.append([start, fin])

time = sorted(time, key=lambda x:(x[0], x[1])) #처음에는  정렬값을 x:x[0]로 설정했지만 이는 같은 시작시간에 있어 끝나는 시간은 순서에 고려되지 않아 문제가 생김

pre = [0, 0]
cnt = 0

for i in time:

    if pre[1] > i[1] and pre[0] < i[0]: #pre값 시간 안에 i가 포함 되어있다면 i로 대체함
        pre = i
        continue

    if i[0] >= pre[1]: #조건에 해당하면 카운트
        cnt += 1
        pre = i

print(cnt) #최종 회의실 수 출력