test = int(input())


for t in range(test) :
    arr = list(map(str, input()))

    Min = int(''.join(arr))
    Max = int(''.join(arr))

    for i in range(len(arr) - 1) :
        for j in range(i+1, len(arr)) :
            if i == 0 and arr[j] == '0' :  
                continue

            arr[i], arr[j] = arr[j], arr[i]

            Min = min(Min, int(''.join(arr)))
            Max = max(Max, int(''.join(arr)))

            arr[j], arr[i] = arr[i], arr[j]

    print(f'#{t+1} {Min} {Max}')

    