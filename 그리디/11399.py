#ATM
import sys
person = int(sys.stdin.readline())
min = list(map(int, sys.stdin.readline().split()))
result = 0
min.sort()

for i in range(person):
    result += sum(min[:(i+1)])

print(result)