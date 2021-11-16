#싸이버 개강총회
import sys
time = list(sys.stdin.readline().replace(":", "").split())

s= int(time[0])
q = int(time[1])
e = int(time[2])
student = dict()
attend = 0

while True:
    try:
        a, a_name = sys.stdin.readline().replace(":","").split()
        if s>= int(a):
            student.get(a_name, 1)
    
        elif q <= int(a) <= e and a_name in student:
            attend += 1
            student[a_name] += 1
        else:
            pass
    
    except ValueError:
        break

for i in student.values():
    if i >= 2:
        attend +=1
print(attend)



# #싸이버 개강총회
# import sys
# from collections import deque
# time = list(sys.stdin.readline().replace(":", "").split())

# s= int(time[0])
# q = int(time[1])
# e = int(time[2])
# student =deque()
# attend = 0

# while True:
#     a, a_name = sys.stdin.readline().split()
    
#     if a=='\n':
#         break

#     a = a.replace(":","")
    
#     if s>= int(a):
#         student.append(a_name)

#     elif q <= int(a) <= e and a_name in student:
#         attend += 1
#         del(student[student.index(a_name)]) 
#     else:
#         pass

# print(attend)
