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


#예산
import sys
n = int(sys.stdin.readline()) #n은 3 이상 10,000 이하
money = list(map(int, sys.stdin.readline().split()))
max_money = int(sys.stdin.readline()) # Max은 n 이상 1,000,000,000 이하

if sum(money) <= max_money:
    print(max(money))

else:
    rev_money = max_money//n
    demand_money = sum(money)//n
    tol_money = sum(money)
    

    while tol_money >= max_money:
        corret = 0
        count = 0 
        for i in money:
            if i < rev_money:
                corret += i

            else:
                corret += rev_money
                count += 1

        tol_money -= count 
        if tol_money >= corret:
            rev_money +=1
        else:
            rev_money -= 1
    
    print(rev_money)
#2안    
    min_num, max_num = 0, max(money)

    while min_num <= max_num:
        mid = (min_num+max_num)//2
        correct = 0
        for i in money:
            correct += min(i, mid)

        if correct < max_money:
            min_num = mid+1
        else:
            max = mid -1
        
    print(mid)

