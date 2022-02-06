#오목
import sys
input = sys.stdin.readline

graph = [list(map(int, input().split())) for _ in range(19)]



move_x = [1, 1, 0, -1]
move_y = [0, 1, 1, 1]

def game():
    for x in range(19):
        for y in range(19):
            if graph[x][y]:
                for i in range(4):
                    test_x = x + move_x[i]
                    test_y = y + move_y[i]
                    cnt = 1

                    if 0 > test_x or test_x >= 19 or 0 > test_y or test_y >= 19:
                        continue
        
                    while 0 <= test_x < 19 and 0 <= test_y < 19 and graph[x][y] == graph[test_x][test_y]:
                        cnt += 1
           
                        if cnt == 5:
                            if 0 <= test_x + move_x[i] < 19 and 0 <= test_y + move_y[i] < 19 and graph[test_x][test_y] == graph[test_x + move_x[i]][test_y + move_y[i]]:    # 육목 판정 1
                                break
                            if 0 <= x - move_x[i] < 19 and 0 <= y - move_y[i] < 19 and graph[x][y] == graph[x - move_x[i]][y - move_y[i]]:    # 육목 판정 2
                                break
                            return graph[x][y], x+1, y+1
                        
                        test_x += move_x[i]
                        test_y += move_y[i]

    return 0, -1, -1


win, idx_x, idx_y = game()
if not win:
    print(win)
else:
    print(win)
    print(idx_x, idx_y)
