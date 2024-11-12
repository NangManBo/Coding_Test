test_case = 10

# for문
for t in range(1, test_case + 1) :
    apt_count = int(input())
    arr = list(map(int, input().split()))
    anw = 0
    for i in range(2, apt_count - 2) :
        # 조건문
        if(arr[i] > arr[i+1] and arr[i] > arr[i + 2] and arr[i] > arr[i - 1] and arr[i] > arr[i - 2] ) :
            l_sub = min(arr[i]-arr[i-1], arr[i]-arr[i-2])
            r_sub = min(arr[i]-arr[i+1],arr[i] - arr[i+2])
            anw+= min(l_sub,r_sub)
    print(f'#{t} {anw}')