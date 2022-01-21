#거북이
import sys
input = sys.stdin.readline

test_c = int(input()) #테스트 갯수


def move_d(i): #방향 회전
    global cnt

    if i == 'L':
        cnt -= 1
        cnt %= 4

    elif i == 'R':
        cnt += 1
        cnt %= 4

    return cnt

def turtle_s(turtle, i): #해당 방향으로 이동
    global cnt
    
    if i == 'B':
        turtle[0] -= move_x[cnt]
        turtle[1] -= move_y[cnt]

    else:
        turtle[0] += move_x[cnt]
        turtle[1] += move_y[cnt]
    
    return turtle

for _ in range(test_c):
    case = list(input().rstrip()) #이동 명령 부분
    move_x = [0, 1, 0, -1] # 이동 x좌표
    move_y = [1, 0, -1, 0] # 이동 y좌표
    cnt = 0                # 방향 조정 변수
    turtle = [0, 0]        #거북이의 현재 위치
    result_x = [0, 0]      #최종 계산에 사용할 x좌표의 최대 최소
    result_y = [0 ,0]      #최종 계산에 사용할 y좌표의 최대 최소
    

    for i in case:
        if i == 'L' or i == 'R': 
            move_d(i)

        elif i == 'B' or i == 'F':
            turtle_s(turtle, i)
            #이동 후 좌표 계산
            result_x[0] = min(turtle[0], result_x[0]) 
            result_x[1] = max(turtle[0], result_x[1])
            result_y[0] = min(turtle[1], result_y[0])
            result_y[1] = max(turtle[1], result_y[1])
        
    print((result_x[1]-result_x[0])*(result_y[1]-result_y[0])) #최종 출력
