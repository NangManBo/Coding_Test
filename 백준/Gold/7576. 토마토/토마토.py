from collections import deque

# 입력
M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 초기 설정
queue = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i, j))  # 익은 토마토 위치를 큐에 추가

# BFS 수행
def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 내에 있고, 익지 않은 토마토인 경우
            if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1  # 하루 더 걸리므로 +1
                queue.append((nx, ny))

# BFS 실행
bfs()

# 결과 계산
max_days = 0
for row in box:
    for tomato in row:
        if tomato == 0:  # 익지 않은 토마토가 남아있는 경우
            print(-1)
            exit()
        max_days = max(max_days, tomato)

# 처음 시작을 1로 했으므로, 최소 일수는 max_days - 1
print(max_days - 1)
