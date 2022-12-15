#[21년 재직자 대회 예선]
#난이더 별3
import sys
input = sys.stdin.readline

n, m, q = map(int, input().split())
graph = [[0]*n for _ in range(m)]
room = {}

for _ in range(q):
    a, b = map(str, input().split())
    if 'In' == a:
        long = len(room)

        if long == 0:
            room[b] = (1, 1)
            graph[0][0] = 1
            print(b, 'gets the seat ',(1, 1)+'.')

            
        else:

    
    elif 'Out' == a:
        


###
# id already seated.
# id already ate lunch.
# id There are no more seats.
# id gets the seat ({x}, {y}).

# id didn't eat lunch.
# id already left seat.
# id leaves from the seat ({x}, {y}).

#  좌석 중 안전도가 가장 높은 좌석이 여럿 있을 수 있다. 이 때는 그 중에서 X가 가장 낮은 좌석을, X도 같다면 Y가 가장 낮은 좌석을 배정해 준다. 특수하게, 현재 모든 좌석이 비어있다면 (1,1)이 배정된다.