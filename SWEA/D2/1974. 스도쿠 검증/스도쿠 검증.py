test_case = int(input())

for t in range(1, test_case + 1) :

    #여기서 1이 글자가 들어갈 수 있는 곳
    arr = [list(map(int, input().split())) for _ in range(9)]
    anw = 1

    # 가로 세로 찾기
    for i in range(9) :
        x_sum = 0
        y_sum = 0
        for j in range(9) :
            x_sum += arr[i][j]
            y_sum += arr[j][i]

        if x_sum != 45 : 
            anw = 0
        if y_sum != 45 : 
            anw = 0

        if(anw == 0) :
            break

    # 3x3 정사각형 시작 지점 느낌
    nx, ny = 0, 0 
    # 정사각형 찾기
    for i in range(9) :
        sum = 0
        for x in range(nx, nx+3) : 
            for y in range(ny, ny+3) :
                sum += arr[x][y]
        
        ny += 3

        if(ny == 9) :
            nx += 3
            ny = 0

        if(sum != 45) :
            anw = 0
            break

    print(f'#{t} {anw}')