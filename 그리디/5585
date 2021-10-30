#거스르돈
pay = int(input()) # 1 이상 1000미만의 정수
coin = [500, 100, 50, 10, 5, 1] # 동전 종류 리스트 
change = 1000-pay # 잔돈

change_coin = 0

for i in coin:
    change_coin += change//i
    change %= i 

print(change_coin)
