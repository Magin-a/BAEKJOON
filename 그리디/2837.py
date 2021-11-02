#설탕배달
sugar = int(input())

bog = 0
while sugar >= 0 :
    if sugar % 5 == 0 :  
        bog += (sugar // 5)  
        print(bog)
        break
    sugar -= 3  
    bog += 1  
else :
    print(-1)