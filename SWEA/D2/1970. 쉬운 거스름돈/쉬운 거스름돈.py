t = int(input())

for test in range(1, t + 1) :
   
    num = int(input())
    
    arr = [50000, 10000, 5000, 1000,500, 100, 50, 10]

    i = 0
    print(f"#{test}")
    while i < 8 :
        p = int(num / arr[i])
        num = int(num % arr[i])
        
        i += 1
        print(p, end=" ")
    print()