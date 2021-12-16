#빈도정렬
import sys

N, C = map(int, sys.stdin.readline().split())
message = list(map(int, sys.stdin.readline().split()))
dic_message = {}

for num in message:
    if num not in dic_message:
        dic_message[num] = 1

    else:
        dic_message[num] += 1
    

sorted_message = sorted(dic_message.items(), key=lambda x:-x[1])
print(sorted_message)
for i in range(len(sorted_message)):
    print((str(sorted_message[i][0]+" ")*sorted_message[i][1],end=""))
