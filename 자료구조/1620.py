#나는야 포켓몬 마스터 이다솜
#자료구조 해시를 이용한 집합과 맵
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

monster = [input().strip() for _ in range(n)]
machine = {a+1: b for a, b in enumerate(monster)}
machine2 = {d:c+1 for c, d in enumerate(monster)}


for _ in range(m):
    quiz = input().rstrip()
    bol = list(quiz)

    if ord(bol[0]) <= 57:
        print(machine[int(quiz)])
    
    else:
        print(machine2[quiz])