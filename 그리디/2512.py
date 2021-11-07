#예산
import sys
n = int(sys.stdin.readline()) #n은 3 이상 10,000 이하
money = list(map(int, sys.stdin.readline().split()))
max_money = int(sys.stdin.readline()) # Max은 n 이상 1,000,000,000 이하


if sum(money) <= max_money:  #총 예산이 max값보다 작다면 가장 큰 예산 출력
    print(max(money))

else:
    test_num = sum(money)//n
    money.append(test_num)
    money.sort()

    a = money.index(test_num)
    del(money[a])

    for x in money[:a]:
        if x <= test_num:
            max_money -= x
       
    result = int(max_money/(n-(a)))
    print(result)




