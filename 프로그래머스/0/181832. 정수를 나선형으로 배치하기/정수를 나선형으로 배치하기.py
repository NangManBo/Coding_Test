def solution(n):
    answer = [[0 for i in range(n)] for j in range(n)]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    # [0][0] -> [0][1]
    # [0][3] -> [1][3]
    # [3][3] -> [3][2]
    
    cx, cy = 0, 0
    change = 0
    answer[0][0] = 1

    # 1 ~ 15 각 + 1씩해서 값 넣어주기
    for i in range(1, n * n + 1) :
        answer[cx][cy] = i
        nx, ny = cx + dx[change], cy + dy[change]
        
        if(n <= nx or n <= ny or 0 > nx or 0 > ny or answer[nx][ny] != 0) :
            change = (change + 1) % 4
            nx, ny = cx + dx[change], cy + dy[change]
        cx,cy = nx,ny
    return answer