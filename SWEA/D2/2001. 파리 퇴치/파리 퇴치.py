t = int(input())

for test_case in range(1, t + 1):
    N, M = list(map(int,input().split()))
    lst = [list(map(int, input().split())) for _ in range(N)]
    
    max = 0
    sum = 0
    for i in range(N - M + 1) :
        for j in range(N - M +1) :
            sum = 0
            for k in range(i, M + i) :
                for n in range (j, M + j) :
                    sum += lst[k][n]                
            if(sum > max) :
                max = sum

    print(f"#{test_case} {max}")
    
    