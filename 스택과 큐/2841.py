# #외계인의 기타연주
# import sys
# n, p = map(int, sys.stdin.readline().split())

# string = [[] for _ in range(n)]
# count = 0

# for _ in range(n):
#     test_s, test_f = map(int, sys.stdin.readline().split())
#     while 1:
#         if not string[test_s-1]:
#             string[test_s-1].append(test_f)
#             count += 1
#             print(string)
#             print("count ->",count)
#             break

#         elif string[test_s-1][-1] == test_f:
#             print(string)
#             print("count ->",count)
#             break

#         else:
#             if string[test_s-1][-1] < test_f:
#                 string[test_s-1].append(test_f)
#                 count += 1
#                 print(string)
#                 break

#             elif string[test_s-1][-1] > test_f:
#                 while string[test_s-1][-1] > test_f:
#                     string[test_s-1].pop()
#                     count += 1
#                     print(string)
#                     print("count ->",count)
#                     if  test_f not in string[test_s-1] and string[test_s-1][-1] > test_f:
#                         string[test_s-1].pop()
#                         count+= 1
#                         string[test_s-1].append(test_f)
#                         print(string)
#                         count += 1
                    

#                     if not string[test_s-1]:
#                         break
#                 break

# print(string)
# print(count)

import sys
n, p = map(int, sys.stdin.readline().split())
string = [[] for _ in range(n)]
count = 0

for _ in range(n):
    test_s, test_f = map(int, sys.stdin.readline().split())
    while True:
        if not string[test_s-1]:
            string[test_s-1].append(test_f)
            count += 1 
            break

        else: 
            if string[test_s-1][-1] < test_f:
                string[test_s-1].append(test_f)
                count += 1
                break

            elif string[test_s-1][-1] == test_f:
                break

            else: #string[test_s-1][-1] > test_f
                while string[test_s-1][-1] > test_f:
                    string[test_s-1].pop()
                    count += 1
                    
                    if not string[test_s-1]:
                        break
                
                if test_f not in string[test_s-1]:
                    string[test_s-1].append(test_f)
                    count += 1

print(count)

