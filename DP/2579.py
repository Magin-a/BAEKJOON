# #계단오르기
# import sys
# num = int(sys.stdin.readline())

# d = [0]*num
# stair = []
# for i in range(num):
#     stair.append(int(sys.stdin.readline()))

# site = 0
# n = -1

# while d[site] != stair[num-1]:
#     d[site] = max(stair[n+1], stair[n+2])
#     site += 1
#     if max(stair[n+1], stair[n+2]) == stair[n]:
#         print(max(stair[n+1], stair[n+2]))
#         n += 1

#     else:
#         print(max(stair[n+1], stair[n+2]))
#         n +=2

# print(d)

import sys
num = int(sys.stdin.readline())

d = [0]*num
stair = []
for i in range(num):
    stair.append(int(sys.stdin.readline()))

d[0] = stair[0]
site = 1
n = 0
treble = 1

while True:
    if max(stair[n+1], stair[n+2]) == stair[n+1] and treble < 2:
        d[site] = stair[n+1] + d[site-1]
        n += 1
        treble += 1
        site += 1

    else:
        d[site] = stair[n+2] + d[site-1]
        treble = 0
        n +=2
        site += 1

    if n == num-1 or n == num-2:
        if n != num-1:
            print(d[site-1])+stair.pop()
            break
        print(d)
        print(d[site-1])
        break


