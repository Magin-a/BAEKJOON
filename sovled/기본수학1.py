# #1712(나의 코드) *
# num= map(int, input().split())
# a,b,c = num
# plus = c-b
# if plus > 0:
#     result =  a//plus+1
    
# else:
#     result = -1
# print(result)

# #2292 *
# num = int(input())
# cnt = 1
# sum = 6
# room_num = 1
# while cnt < num:
    
#     cnt += sum
#     sum +=6
#     room_num += 1
# print(room_num)

# #1193
# my_num = int(input())
# num_cnt = 1
# count = 1
# while my_num > num_cnt:
#     count += 1
#     num_cnt +=count
# result_index = num_cnt - count
# if count%2 == 1:
#     numerator =  count      #분자
#     denominator =  1    #분모
#     result_index += 1
#     gap =  my_num - result_index
#     numerator -= gap
#     denominator += gap

# else:
#     numerator = 1
#     denominator = count
#     result_index += 1
#     gap =  my_num - result_index
#     numerator += gap
#     denominator -= gap

# print("{0}/{1}".format(numerator, denominator))
# #1193 
# n,i = int(input()), 1
# while n>0:
#     n -= i
#     i += 1
# print(n, i)
# if i%2 == 0: 
#     print(f'{1-n}/{n+i-1}')
# else:
#     print(f'{n+i-1}/{1-n}')

# #2867
# x = map(int, input().strip().split())
# A, B, V= x
# day = 0
# location = 0
# while V > location:
#     day += 1
#     location += A
#     if  V > location:
#         location -= B
#     else:
#         pass
    
    
# print(day)

# # #2867
# A, B, V = map(int, input().split())
# day = 0      

# if (V-B) % (A-B) != 0:
#     day = ((V-B) // (A-B)) + 1
# else:
#     day = ((V-B) // (A-B))
# print(day)

# #10250
# test = int(input())
# for customer_num in range(1, test+1):
#     floor, room, customer = map(int, input().split())
#     if customer%floor == 0:
#         customer_floor = str(customer)
#         customer_room = str((customer//floor))
#         customer_room = (customer_room.zfill(2))
#         result = customer_floor+customer_room
#     else:
#         customer_floor = str(customer%floor)
#         customer_room = str((customer//floor)+1)
#         customer_room = (customer_room.zfill(2))
#         result = customer_floor+customer_room
    
#     print(result)



# t=int(input())

# for i in range(t):
  
#   h,w,n=map(int,input().split())

  
#   line=n//h+1
  
#   if n%h==0:
#     floor=h
#     line=n//h
#   else:
#     floor=n%h
  
#   answer=floor*pow(10,2)+line
#   print(answer)

# #2775
# t = int(input())
# for i in range(t):
#     floor = int(input())
#     num = int(input())
#     result_list = []
#     floor_list =[]
#     floor_list2 =[]
#     #0층 사람 수
#     for x in range(1, num+1):
#         floor_list.append(x) 
#     result_list.append(floor_list)
#     for y in range(num):
#             floor_list2.append(sum(floor_list[0:y+1]))
#     result_list.append(floor_list2)

    
#     #2층부터 ~floor까지
#     for _ in range(floor-2):
#         for z in range(num):
#             floor_list2.append(sum(floor_list2[0:z+1]))


#         result_list.append(floor_list2)
#         print(floor_list2)



# #2755 나의  해답
# t= int(input())
# for _ in range(t):
#     floor = int(input())
#     room = int(input())
#     result = []
#     person_list = []
#     for i in range(1, room+1):
#         person_list.append(i)
#     result.append(person_list)
#     for y in range(floor):
#         person_list = []
#         for z in range(1, room+1):
#             person_list.append(sum(result[y][0:z]))
#         result.append(person_list)
#     print(result[floor][room-1])


# #2839
# sugar = int(input())

# bol = 0
# while sugar >= 0 :
#     if sugar % 5 == 0 :  # 5의 배수이면
#         bol += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
#         print(bol)
#         break
#     sugar -= 3  
#     bol += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
# else :
#     print(-1)

# # #2839
# weight = int(input())
# bol = 0
# b0l5 = 0
# bol3 = 0

# if weight%2 == 1:
#     5*((weight//5)+1) 
# elif weight%2 == 0:
 

# #1011
# test_num = int(input())


# for _ in range(test_num):
#     jump = 1
#     cnt = 0
#     start, fin = map(int, input().split())
    
#     while start < fin:
#         start += jump
#         if fin == start or fin < start :
#             cnt +=1
            
#         elif fin == start+1:
#             start += 2
#             break

#         else:
#             cnt += 1
#             jump += 1
        
    
#     print(cnt)
a = 1
while a < 4:
    a +=1 
    print(1) 

        



# import sys
# n = int(input())
# b = list(sys.stdin.readline().split())
# result = 0
# for i in b:
#     num = 0
#     for ii in range(1,int(i)+1):
#         if int(i) % ii == 0:
#             num += 1
#     if num == 2 :
#         result += 1
#         num = 0

# print(result)