#1978
cnt = int(input())
num = list(map(int, input().split()))
result = 0

for i in num:
    mid = 0
    for div in range(1, i+1):
        if i % div == 0:
            mid += 1
            
    if mid == 2 :
        result += 1
        mid = 0

print(result)