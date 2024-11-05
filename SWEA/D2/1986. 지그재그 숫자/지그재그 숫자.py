t = int(input())

for test in range(1, t + 1) :
   
    num = int(input())

    anw = 0
    for i in range(1, num + 1) :
        if(i % 2 == 0) :
            anw -= i
        else :
            anw += i
    
    print(f"#{test}", anw)
    
