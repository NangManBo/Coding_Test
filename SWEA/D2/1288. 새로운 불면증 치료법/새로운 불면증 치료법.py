test = int(input())

for t in range(1, test + 1) :
    anw = 0
    num = int(input())
    arr = [0 for _ in range(10)]
    i = 0

    while sum(arr) < 10 :
        i += 1
        a = num * i

        lis = list(map(int ,str(a)))
        for j in range(len(lis)) :
            if(int(lis[j]) == 0 and arr[0] == 0) :
                arr[0] = 1
            elif(int(lis[j]) == 1 and arr[1] == 0) :
                arr[1] = 1
            elif(int(lis[j]) == 2 and arr[2] == 0) :
                arr[2] = 1
            elif(int(lis[j]) == 3 and arr[3] == 0) :
                arr[3] = 1
            elif(int(lis[j]) == 4 and arr[4] == 0) :
                arr[4] = 1
            elif(int(lis[j]) == 5 and arr[5] == 0) :
                arr[5] = 1
            elif(int(lis[j]) == 6 and arr[6] == 0) :
                arr[6] = 1
            elif(int(lis[j]) == 7 and arr[7] == 0) :
                arr[7] = 1
            elif(int(lis[j]) == 8 and arr[8] == 0) :
                arr[8] = 1
            elif(int(lis[j]) == 9 and arr[9] == 0) :
                arr[9] = 1
        anw = a
    print(f"#{t} {anw}")
