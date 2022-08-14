# 별 찍기 - 10
# 분할정복, 재귀
import sys
input = sys.stdin.readline

n = int(input())

def star(x):
    if x ==3:
        return ['***', '* *', '***']

    arr = star(x//3)
    result = []

    for i in arr:
        result.append(i*3)

    for i in arr:
        result.append(i+' '*(x//3)+i)

    for i in arr:
        result.append(i*3)

    return result
    
print('\n' .join(star(n)))