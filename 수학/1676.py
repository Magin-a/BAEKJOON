#팩토리얼 0의 개수
#수학 
import sys
input = sys.stdin.readline

num = int(input())
cnt = 0

def factorial(num):
    if num>1:
        return num*factorial(num-1)

    else:
        return 1

a = str(factorial(num))
for i in a[::-1]:
    if i == '0':
        cnt += 1

    else:
        break
print(cnt)