#창고 다각형
import sys
input = sys.stdin.readline

n = int(input())
case = [0]*1001
result = 0
max_data = 0
max_idx = 0
end_idx = 0

for _ in range(n): #입력부
    index, length = map(int, input().split())
    case[index] = length
    if max_data < length: #입력중에 가장 큰 data와 index 갱신
        max_data = length
        max_idx = index
    end_idx = max(index, end_idx) #마지막 값 index

case1 = 0
for a in range(0, max_idx): # max_idx 기준 왼쪽 계산
    if case[a] == 0 and case1 == 0: #처음에 나오는 빈칸 제거
        continue

    else:
        case1 = max(case[a], case1) #이전 값중 큰것을 result에 더하기
        result += case1
#가장큰값 더하기
result += max_data

# max_idx 기준 오른편 계산
case1 = 0
for b in range(end_idx, max_idx, -1): #왼쪽과 같은 방식 끝에서부터 max_idx까지  
    case1 = max(case1, case[b])
    result += case1

#최종 출력
print(result)
