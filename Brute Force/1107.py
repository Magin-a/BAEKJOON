#리모컨
#Brute Force
#채널 시작점은 100이다.
import sys
input = sys.stdin.readline
#입력부
g_cannel = int(input())
broken_cnt = int(input())
b_list = list(map(int, input().split()))

#+,- 채널이동만으로 옮긴 횟수
min_result = abs(100-g_cannel)

for a in range(1000001):
    num = str(a)#바로 아래 for문을 위해 문자열 취급

    for i in range(len(num)):
        if int(num[i]) in b_list: #해당수에 부서진 숫자가 있다면 다음 순번으로
            break

        elif i == len(num)-1: #최소값 갱신
            min_result = min(min_result, abs(int(num)-g_cannel)+ len(num))

print(min_result)