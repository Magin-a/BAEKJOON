#창고 다각형
import sys
input = sys.stdin.readline

n = int(input())
case = [0]*1001
result = 0
max_data = 0
max_idx = 0
end_idx = 0

for _ in range(n):
    index, length = map(int, input().split())
    case[index] = length
    if max_data < length:
        max_data = length
        max_idx = index
    end_idx = max(index, end_idx)

case1 = 0
for a in range(0, max_idx):
    if case[a] == 0 and case1 == 0:
        continue

    else:
        case1 = max(case[a], case1)
        result += case1
result += max_data
case1 = 0
for b in range(end_idx, max_idx, -1):
    case1 = max(case1, case[b])
    result += case1
print(result)
