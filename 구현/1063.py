#킹
import sys
k, s, n = sys.stdin.readline().split()
move_x, move_y = [0, 0, -1, 1, 1, 1, -1, -1], [1, -1, 0, 0, 1, -1, 1, -1]
move_index = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']

king_x, king_y = int(k[1]), ord(k[0])-64
stone_x, stone_y = int(s[1]), ord(s[0])-64
for _ in range(int(n)):
    num = move_index.index(sys.stdin.readline().strip())
    test_x = king_x+move_x[num]
    test_y = king_y+move_y[num]

    if 1 > (test_x) or (test_x) > 8 or (test_y) <1 or (test_y) >8:
        continue
    
    if test_x == stone_x and test_y == stone_y: 
        t_stone_x = stone_x + move_x[num]
        t_stone_y = stone_y + move_y[num]
            
        if 1 >t_stone_x or t_stone_x >8 or t_stone_y < 1 or t_stone_y > 8:
            continue
        
        stone_x, stone_y = t_stone_x, t_stone_y
        king_x, king_y = test_x, test_y
    
    king_x, king_y = test_x, test_y

    

print(chr(king_y+64)+str(king_x))
print(chr(stone_y+64)+str(stone_x))



#행렬방법으로 구현했기에 위아래 이동은 반대
# R : 한 칸 오른쪽으로
# L : 한 칸 왼쪽으로
# T : 한 칸 아래로
# B : 한 칸 위로
# RB : 오른쪽 위 대각선으로
# LB : 왼쪽 위 대각선으로
# RT : 오른쪽 아래 대각선으로
# LT : 왼쪽 아래 대각선으로
