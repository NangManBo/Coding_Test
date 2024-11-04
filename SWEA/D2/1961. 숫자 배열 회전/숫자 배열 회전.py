test_case = int(input())

for t in range(1, test_case + 1) :

    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]
    anw = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]

    for x in range(3) :
        for y in range(n) :
            for z in range(n) :
                anw[x][z][n-y-1] = arr[y][z]
        for a in range(n) :
            for b in range(n) :
                arr[a][b] = anw[x][a][b]          
    print(f"#{t}")

    for i in range(n) :
        for j in range(3):
            for k in range(n) :
                print(anw[j][i][k], end="")
            print(end=" ")
        print()
            