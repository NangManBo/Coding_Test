from collections import deque

# 입력 및 초기화
L, N, M = map(int, input().split())
toma = [[list(map(int, input().split())) for _ in range(N)] for _ in range(M)]
queue = deque()

# 초기 익은 토마토 위치 큐에 추가
for i in range(M):
    for j in range(N):
        for k in range(L):
            if toma[i][j][k] == 1:
                queue.append((i, j, k))  # (z, y, x) 형태로 추가

# BFS 함수 정의
def BFS():
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    while queue:
        z, y, x = queue.popleft()
        
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= nz < M and 0 <= ny < N and 0 <= nx < L:
                if toma[nz][ny][nx] == 0:
                    toma[nz][ny][nx] = toma[z][y][x] + 1
                    queue.append((nz, ny, nx))

# BFS 실행
BFS()

# 결과 계산
max_days = 0
for layer in toma:
    for row in layer:
        for tomato in row:
            if tomato == 0:  # 익지 않은 토마토가 남아 있는 경우
                print(-1)
                exit()
            max_days = max(max_days, tomato)

print(max_days - 1)
