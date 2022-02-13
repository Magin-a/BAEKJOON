#시리얼 번호
import sys
input = sys.stdin.readline
n = int(input())

data = [input().rstrip() for _ in range(n)]

def f(a):
    result = 0
    for i in a:
        if i.isdigit(): #숫자가 있다면?
            result += int(i)

    return result

data.sort(key=lambda x:(len(x), f(x), x)) #조건(길이, 숫자총합, 알파벳)
for x in data:
    print(x)
