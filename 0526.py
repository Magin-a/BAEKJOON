# #2739
# a = int(input())
# for i in range(1, 10):
#     result = a * i
#     print(a,'*',i,'=', result)

# #10950
# num = int(input())

# for i in range(num):
#     x = map(int, input().split())
#     a, b = x
#     print(a+b)

# #8393
# num = int(input())
# result = 0
# for i in range(1,num+1):
#     result += i
# print(result)

# #2741
# num = int(input())
# result = num+1
# for i in range(num):
#     result -= 1
#     print(result)

# #2439
# a = int(input())
# for i in range(a):

# #11021
# a = int(input())
# n = 0
# for i in range(a):
#     x = map(int, input().split())
#     a,b = x
#     n += 1
#     print("Case #{0}: {1}".format(n, a+b))

# #11022
# a = int(input())
# n = 0
# for i in range(a):
#     x = map(int, input().split())
#     a,b = x
#     n += 1
#     print("Case #{0}: {1} + {2} = {3}".format(n, a, b, a+b))

# # 10871
# x = map(int, input().split())
# y = list(map(int, input().split()))
# a, b = x

# for i in range(a):
#     if y[i] < b:
#         print(y[i], end=' ')

# #10952
# a, b = 1, 1
# while a != 0 and b != 0:
#     x = map(int, input().split())
#     a,b = x
#     if a == 0 and b == 0:
#         pass
#     else:
#         print(a+b)

# #1110 (미해결)
# a = int(input())

# n = 0
# num1 = a//10
# num2 = a%10
# x = num1 +num2
# while str(a) != str(x)+str(num2):
#     if x < 10:
        
#         x = num2 + x
#         num2 = x
#         if x >= 10:
#             num2 = x%10
        
#     elif x >= 10:
#         x = num2 + (x%10)
#         num2 = x




    # num1 = x/10
    # num2 = x%10
    # x = num1 +num2
    # n += 1
    # if a < 10:
    #     a = num2 + a
    # elif a >= 10:
    #     a = num2 + (a%10)

    





