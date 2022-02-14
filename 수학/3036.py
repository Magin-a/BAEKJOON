#링
import sys

input = sys.stdin.readline
n = int(input())
ring = list(map(int, input().split()))
std = ring[0]
data = ring[1:]

def cal(a, b):
    while b != 0:    
        num = a%b
        a = b
        b = num
    return a

for x in data:
    result = cal(std, x)
    print(f"{std//result}/{x//result}")
