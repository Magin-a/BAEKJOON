#숫자고르기
import sys
input = sys.stdin.readline

num = int(input())

graph = [n for n in range(0,num+1)]
bol = [0] # 번호순 1~n을 맞ㅇ춰주기 위한 index0값의 데이터는 0
result= set()
for _ in range(num):
    bol.append(int(input())) #해당 번호값에 맞게 설정

def dfs(first, second, num):
    first.add(num) #첫줄 집합 추가
    second.add(bol[num]) #두번째줄 집합 추가
    if bol[num] in first:
        if  first == second: #조건에 충족된다면 result 갱신
            result.update(first)
            return True
        return False
    return dfs(first, second, bol[num]) 

for i in range(1,num+1): #1~n까지 탐색
    if i not in result: #해당 번호가 탐색
        dfs(set(), set(), i)
print(len(result))
print(*sorted(list(result)), sep="\n")