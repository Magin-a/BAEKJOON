#Fly me to the Alpha Centauri
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    start, fin = map(int, input().split())
    len = fin-start

    print(int((len*4-3)**.5))
