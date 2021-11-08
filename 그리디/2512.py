#예산
import sys
n = int(sys.stdin.readline()) #n은 3 이상 10,000 이하
money = list(map(int, sys.stdin.readline().split()))
max_money = int(sys.stdin.readline()) # Max은 n 이상 1,000,000,000 이하

if sum(money) <= max_money:# 요청 예산의 총합 < 가능한 총예산일 경우 요청 예산의 가장 큰 액수 출력
    print(max(money))

else:
    min_num, max_num = 0, max(money) 
    
    while max_num >= min_num: # max_money에 도달할때까지 반복
        mid = (max_num+min_num)//2 # 기준점 생성
        correct = 0 #반복문 중 예산을 저장

        for i in money: #반복문으로 예산 배정
            if mid >= i: #기준점보다 작은 값은 예산 통과
                correct += i
            else: #문제가 되는 예산은 한계선인 mid으로 대체
                correct += mid

        if correct > max_money: #배정 예산 > 가능한 총 예산 일 경우 
            max_num = mid -1  #가장 큰 값을 -1 해준다

        else:  #배정예산 < 가능한 총 예산 일 경우  
            min_num = mid +1 # 가장 작은 값에서 +1 해준다
    print(max_num) #while 종료후 값 출력
