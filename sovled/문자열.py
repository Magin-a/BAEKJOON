#1157
my_test = input().upper()
result = list(my_test)
result_set = set(result)
count_list = []
count_word = []
for a in result_set:
    word_count = 0
    x = my_test.count(a)
    count_list.append(int(x))
    count_word.append(a)
if count_list.count(max(count_list)) >= 2:
    print("?")
else:
    print(count_word[count_list.index(max(count_list))])

#1152
a = input().split()
print(len(a))

#2908
num = map(str, input().split())
a, b = num
a = int(a[::-1])
b = int(b[::-1])

print(max(a,b))

#5622
a = list(input())
result = 0
for i in a:
    if i in ('A','B','C'):
        result += 3
    elif i in ('D','E','F'):
        result += 4
    elif i in ('G','H','I'):
        result += 5
    elif i in ('J','K','L'):
        result += 6
    elif i in ('M','N','O'):
        result += 7
    elif i in ('P','Q','R','S'):
        result += 8
    elif i in ('T','U','V'):
        result += 9
    elif i in ('W','X','Y','Z'):
        result += 10
print(result)

#2941
word = ["c=","c-","dz=","d-","lj","nj","s=","z="]
cnt = 0
cnt2 = 0
a = input()
letter = a
for i in word:
    if i in a:
        cnt += a.count(i)
        a = a.replace(i,' ')
    else:
        pass
a = a.split(' ')
for j in a:
    cnt2 += len(j) 
print(cnt+cnt2)
#추가풀이
C=["c=","c-","dz=","d-","lj","nj","s=","z="]
s=input()
for i in C:s=s.replace(i,"!")
print(s)
print(len(s))


#1712
num= map(int, input().split())
a,b,c = num
plus = c-b
if plus > 0:
    result =  a//plus+1
    
else:
    result = -1
print(result)

num = map(int, input().split())
a, b = num
print(a+b)

#10809
a = input()
Eng = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
start_num = 0
for i in a:
    if i in Eng:
        if num[Eng.index(i)] == -1: 
            num[Eng.index(i)] = start_num
            
        else:
            pass
    start_num += 1
for j in num:
    print(j, end=' ')

2292

