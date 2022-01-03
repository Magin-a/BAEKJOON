# #봄버맨
import sys
from collections import deque

move = [[-1,0],[1, 0],[0, -1],[0, 1]]

def col_boom():
    for index_1 in range(r):
        for index_2 in range(c):
            if graphy[index_1][index_2] == 'O':
                boom.append([index_1, index_2])

def all_boom():
    for index_1 in range(r):
            for index_2 in range(c):
                if graphy[index_1][index_2] == '.':
                    graphy[index_1][index_2] = 'O'

def boom_boom():
    while boom:
        boom_x, boom_y = boom.popleft()
        graphy[boom_x][boom_y] = '.'
        for move_x, move_y in move:
            test_x, test_y = boom_x+move_x, boom_y+move_y
            if 0 <= test_x < r:
                result_x = test_x
            else:
                result_x = boom_x

            if 0 <= test_y < c:
                result_y = test_y
            else:
                result_y = boom_y
            if graphy[result_x][result_y] == 'O':
                graphy[result_x][result_y] = '.'

r, c, n = map(int, sys.stdin.readline().split())
graphy = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
boom = deque()

n -= 1

while n:
    col_boom()
    if n == 0:
        break
    
    n -= 1
    all_boom()
    if n == 0:
        break

    n -= 1
    boom_boom()
    

for a in graphy:
    for b in a:
        print(b, end='')
    print() 
