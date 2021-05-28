#1110
a = int(input())

n = 1
num1 = a//10
num2 = a%10
x = num1 +num2
n = 1
while a != int(str(num2)+str(x%10)):
    if x < 10:
        num1 =x%10
        x = num1 + num2
        num2 = num1
        n +=1
        
    elif x >= 10:
        num1 =x%10
        x = num1 + num2
        num2= num1
        n +=1

print(n)


#2562
result = []
for i in range(9):
    result.append(int(input()))

print(max(result))
print(result.index(max(result))+1)

#2577
a = int(input())
b = int(input())
c = int(input())
num_x = b%(10*1)
num1 = a * (num_x)
num2 = a * ()



