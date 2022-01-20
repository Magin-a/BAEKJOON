#거북이
import sys
input = sys.stdin.readline

test_c = int(input())


def move_d(i):
    global cnt

    if i == 'L':
        if cnt == 0:
            cnt = len(move) - 1
        
        else:
            cnt -= 1

    elif i == 'R':
        if cnt == 3:
            cnt = 0
        else:
            cnt += 1

    return cnt

def turtle_s(turtle, i):
    global cnt
    
    if i == 'B':
        turtle[0] -= move[cnt][0]
        turtle[1] -= move[cnt][1]

    else:
        turtle[0] += move[cnt][0]
        turtle[1] += move[cnt][1]
    
    return turtle

for _ in range(test_c):
    case = list(input().rstrip())
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    cnt = 0
    turtle = [0, 0]
    turtle_status = move[cnt]
    result_x , result_y= [0, 0], [0, 0]#x좌표 최대최소, y좌표 최대최소

    for i in case:
        if i == 'L' or i == 'R':
            move_d(i)

        elif i == 'B' or i == 'F':
            turtle_s(turtle, i)
            if turtle[0] > result_x[1]:
                result_x[1] = turtle[0]

            elif turtle[0] < result_x[0]:
                result_x[0] = (turtle[0])

            if turtle[1] > result_y[1]:
                result_y[1] = turtle[1]

            elif turtle[1] < result_y[0]:
                result_y[0] = (turtle[1])
            
        result_x[0], result_y[0] = abs(result_x[0]), abs(result_y[0])
    print(sum(result_x)*sum(result_y))
