test_case = int(input())

for t in range(1, test_case + 1) :

    N, K = map(int, input().split())
    #여기서 1이 글자가 들어갈 수 있는 곳
    toma = [list(map(int, input().split())) for _ in range(N)]
    anw = 0

    # 가로 테스트
    for i in range(N) :
        x_count = 0
        y_count = 0
        for j in range(N) :
            if(x_count == K and toma[i][j] == 0) :   
                anw += 1
                x_count = 0
            if toma[i][j] == 1 : 
                x_count += 1
            elif toma[i][j] == 0 or x_count >= K + 1: 
                x_count = 0
            if(y_count == K and toma[j][i] == 0) :   
                anw += 1
                y_count = 0
            if toma[j][i] == 1 : 
                y_count += 1
            elif toma[j][i] == 0 or y_count >= K + 1 : 
                y_count = 0
        if x_count == K :
            anw += 1
        if y_count == K :
            anw += 1

    print(f'#{t} {anw}')