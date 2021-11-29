#스택(10828)
import sys
n = int(sys.stdin.readline())

ary=[]

for _ in range(n):
    
    comand = sys.stdin.readline().split()
    
    if comand[0] == 'push':
        ary.append(comand[1])
        

    if comand[0] == 'pop':
        if len(ary) == 0:
            print(-1)
            

        else:
            print(ary.pop())
            

    if comand[0] == 'top':
        if len(ary) == 0:
            print(-1)
            
        else:
            print(ary[-1])
            

    if comand[0] == 'size':
        print(len(ary))
        

    if comand[0] == 'empty':
        if len(ary) == 0:
            print(1)
            
        else:
            print(0)
