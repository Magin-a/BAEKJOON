#안테나
import  sys
n = int(sys.stdin.readline()) 
house = list(map(int, sys.stdin.readline().split()))
#여기까지 입력라인

house.sort() #크기 비교를 위한 정렬

print(house[(n-1)//2]) #index 값 0부터 시작이므로 n-1로 비교 출력
