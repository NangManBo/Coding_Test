i = int(input())

for k in range(1, i+1) : 
    arr = list(map(int,input().split()))

    if(arr[0] > arr[1]) :
        print(f"#{k} >")
    elif (arr[0] == arr[1]) :
        print(f"#{k} =")
    else :
        print(f"#{k} <")

