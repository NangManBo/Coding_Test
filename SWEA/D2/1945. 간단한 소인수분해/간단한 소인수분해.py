test_case = int(input())

for t in range(1, test_case + 1) :
    num = int(input())
    arr = [0 for i in range(5)]
    
    while num > 1 :
        if(num % 2 == 0 ) :
            arr[0] += 1
            num = int(num / 2)
        elif(num % 3 == 0 ) :
            arr[1] += 1
            num = int(num / 3)
        elif(num % 5 == 0 ) :
            arr[2] += 1
            num = int(num / 5)
        elif(num % 7 == 0 ) :
            arr[3] += 1
            num = int(num / 7)
        elif(num % 11 == 0 ) :
            arr[4] += 1
            num = int(num / 11)
    
    print(f"#{t}", end=" ")
    for i in range(len(arr)) :
        print(arr[i], end = " ")
    print()