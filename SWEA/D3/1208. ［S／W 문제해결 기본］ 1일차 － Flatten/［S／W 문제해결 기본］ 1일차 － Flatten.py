for t in range(10) :
    count = int(input())
    arr = list(map(int,input().split()))
    anw = 0

    for i in range(count) :
        max_index = arr.index(max(arr))
        min_index = arr.index(min(arr))

        arr[max_index] -= 1
        arr[min_index] += 1

    anw = arr[arr.index(max(arr))] - arr[arr.index(min(arr))]
    print(f"#{t+1} {anw}")
