def solution(board):
    answer = 0
    l = len(board[0])
    
    visited = [[0 for _ in range(l)] for _ in range(l)]
    dirx = [-1,-1,-1, 0, 0, 1, 1, 1]
    diry = [-1, 0, 1,-1, 1,-1, 0, 1]
    
    for i in range(l) :
        for j in range(l) :
            if(board[i][j] == 1) :
                visited[i][j] = 1
                print('폭탄',i,j)
                for k in range(8) :
                    ni,nj = i + dirx[k],j +diry[k]
                    if(0<=ni <l and 0<=nj<l) :
                        print(ni,nj)
                        visited[ni][nj] = 1
        
    for n in visited :
        for m in range(len(n)) :
            if(n[m] == 0) :
                answer += 1
    
    return answer