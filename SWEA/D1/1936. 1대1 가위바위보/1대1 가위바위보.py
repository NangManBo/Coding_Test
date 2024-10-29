
arr = list(map(int,input().split()))

for i in range(1, 2) :
    if(arr[0] > arr[1]) :
        if(arr[0] == 3) : 
            if(arr[1] == 1) : 
                print('B')
            else :
                print("A")
        elif(arr[0] == 2) :
            print("A")
    elif(arr[0] < arr[1]) :
        if(arr[1] == 3) : 
            if(arr[0] == 1) : 
                print('A')
            else :
                print("B")
        elif(arr[1] == 2) :
            print("B")
