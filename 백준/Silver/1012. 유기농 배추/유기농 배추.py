from collections import deque

t = int(input())


def solution() :
    anwser = []
    for i in range(N) :
        for j in range(M):
            if(arr[i][j] == 1 and visited[i][j] == False) :
                anwser.append(BFS(i,j))
    print(len(anwser))


def BFS(i,j) :
    queue = deque([(i,j)])
    visited[i][j] = True
    component = []

    while queue :
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        x , y =queue.popleft()
        component.append((x , y))
        
        for i in range(4) : 
            nx = x + dx[i]
            ny = y + dy[i]
            if(0 <= nx < N and 0 <= ny < M ) :
                if(arr[nx][ny] == 1 and  visited[nx][ny] == False) :
                    visited[nx][ny] = True
                    queue.append((nx,ny))

    return component

for test in range(1, t + 1) :
   
    N,M,K = map(int, input().split())

    # M이 세로 N이 가로 
    arr = [[0 for i in range(M)] for i in range(N)]
    visited = [[False for i in range(M)] for i in range(N)]

    for _ in range(K) :
        x,y = map(int, input().split())
        arr[x][y] = 1

    solution()