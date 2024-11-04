t = int(input())

for test in range(1, t + 1) :
    N, M = map(int, input().split())

    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    max = 0
    if(N > M) :
        for i in range(N - M + 1) :
            sum = 0
            for j in range(M) :
                sum += B[j] * A[i+j]
            if(sum > max) :
                max = sum
    if(N < M) :
        for i in range(M - N + 1) :
            sum = 0
            for j in range(N) :
                sum += A[j] * B[i+j]
            if(sum > max) :
                max = sum

    print(f"#{test}", max)
   