#경비원
# import sys
# length, width = int(sys.stdin.readline().split())
# n = int(sys.stdin.readline())

# store = []
# for _ in range(n):
#     store.append(sys.stdin.readline().split())

# dong_x, dong_y = int(sys.stdin.readline())

# result = 0
# a = [[1,2, width, length], [2,1, width, length], [3,4, length, width], [4,3, length, ]]

# for x, y in store:
#     if dong_x == x:
#         result += abs(y-dong_y)

#     elif [x, dong_x] in a:
#         site = a.index([x, dong_x])
#         result += min((

#경비원
import sys
from collections import deque
length, width = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())

result = 0
store = deque()
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    if x  == 1:
        store.append([0,y])

    elif x == 2:
        store.append([width, y])
    
    elif x == 3:
        store.append([y, 0])

    elif x == 4:
        store.append([y, length])

pol_x, pol_y = map(int, sys.stdin.readline().split())
if pol_x == 1:
    pol_x = 0

elif pol_x == 2:
    pol_x = width

elif x == 3:
    pol_x, pol_y = y, 0 

elif x == 4:
    pol_x, pol_y = y, length


while store:
    test_x, test_y = store.popleft()
    
    


