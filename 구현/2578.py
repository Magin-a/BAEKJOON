#빙고
import sys
from collections import deque
input = sys.stdin.readline

board = [input().split() for _ in range(5)]
call = []

for _ in range(5):
    call += input().split()

def bingo_find(board):
    cnt = 0

    #가로
    for a in board:
        if a.count(0) == 5:
            cnt += 1
            

    #세로
    for x in range(5):
        h = 0
        for y in range(5):
            if board[y][x] == 0:
                h +=1

        if h == 5:
            cnt += 1
            

    # 대각선(\) 확인
    k = 0
    for i in range(5): 
        if board[i][i] == 0:
            k += 1
    if k == 5:
        cnt += 1
    # 대각선(/) 확인
    u = 0
    for i in range(5): 
        if board[i][4-i] == 0:
            u += 1
    if u == 5:
        cnt += 1
                
    return cnt

for  idx, call_data in enumerate(call):
    for line in board:
        if call_data in line:
            line[line.index(call_data)] = 0
            break

    find = bingo_find(board)

    if find >= 3:
        print(idx+1)
        break
