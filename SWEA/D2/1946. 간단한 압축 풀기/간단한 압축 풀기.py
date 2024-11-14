test = int(input())

for t in range(1, test+1) :
    n = int(input())
    count = 0
    
    print(f"#{t}")
    for i in range(n) :
        arr = list(map(str, input().split()))

        for i in range(int(arr[1])) :
            count += 1
            print(arr[0], end="")
            if(count == 10) :
                count = 0
                print()
    print()
            
