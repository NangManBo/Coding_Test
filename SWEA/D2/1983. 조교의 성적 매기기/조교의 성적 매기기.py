t = int(input())

for test in range(1, t + 1) :
    N, M = map(int, input().split())
    count = int(N / 10)
    stu = [list(map(int,input().split())) for _ in range(N)]
    avg = [[0] for _ in range(N)]
    grade = ["A+", "A0", "A-", "B+","B0","B-","C+","C0","C-","D0"]
    anw = [[]for _ in range(N)]
    
    for i in range(N) :
        avg[i] = stu[i][0] * 0.35 + stu[i][1] * 0.45 + stu[i][2] * 0.20

    k = 0
    for i in range(int(N /count)) :
        for j in range(count) :
            num = avg.index(max(avg)) #성적 계산 한 것들 중에서 최대값
            anw[num] = grade[k]
            avg[num] = 0
        k += 1
    
    print(f"#{test} {anw[M-1]}")
    
