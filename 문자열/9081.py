import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    spelling = input().strip()
    bol= []
    for i  in spelling:
        bol.append(ord(i)-64)
    
    test = bol.pop()

    for a in range(len(bol)-1, -1, -1):
        if test > bol[a]:
            bol.insert(a, test)
            test = None
            break

        else:
            pass
    
    if test != None:
        bol.append(test)
    
    for q in bol:
        print(chr(q+64),end='')
    print('\n')
