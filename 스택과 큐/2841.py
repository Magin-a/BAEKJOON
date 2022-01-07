# #외계인의 기타연주
import sys
n, p = map(int, sys.stdin.readline().split())  #줄과 프렛 입력
string = [[] for _ in range(n)] #줄 갯수만큼 
count = 0 #손가락을 움직이는 횟수

for _ in range(n): #n개만큼 입력
    test_s, test_f = map(int, sys.stdin.readline().split()) 
    while True:
        #해당 줄에 이전 입력이 없다면
        if not string[test_s-1]:
            string[test_s-1].append(test_f)
            count += 1 
            break
        
        #이전 입력이 있었다면
        else: 
            #입력 음이 이전보다 크다면
            if string[test_s-1][-1] < test_f:
                string[test_s-1].append(test_f)
                count += 1
                break
            #입력음이 이전과 같다면
            elif string[test_s-1][-1] == test_f:
                break
            #입력음이 이전보다 작다면(string[test_s-1][-1] > test_f)
            else: 
                #입력음 보다 큰음이 없을 때까지 pop()
                while string[test_s-1][-1] > test_f:
                    string[test_s-1].pop()
                    count += 1
                    #중간에 안전장치
                    if not string[test_s-1]:
                        break
                #바로 위 반복문에서 탈출해서 입력음이 없다면
                if test_f not in string[test_s-1]:
                    string[test_s-1].append(test_f)
                    count += 1

print(count) #최종 출력