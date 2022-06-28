#성적평균
#학번 구간 [A, B]가 주어졌을 때 이 학생들 성적의 평균을 구하는 프로그램을 작성하라.
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
score = list(map(int, input().split()))

def aver(a,b):
    result = round(sum(score[a-1:b])/(b-a+1), 3)
    print('%0.2f' %result)
for _ in range(k):
    a, b = map(int, input().split())
    aver(a,b)