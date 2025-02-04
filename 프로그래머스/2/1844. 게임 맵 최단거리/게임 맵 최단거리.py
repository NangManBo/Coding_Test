from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])  # 맵 크기 (행: n, 열: m)
    dx = [1, -1, 0, 0]  # 상하좌우 이동
    dy = [0, 0, 1, -1]

    queue = deque([(0, 0)])  # (x, y) 위치를 큐에 삽입

    while queue:
        cx, cy = queue.popleft()  # 현재 위치 꺼내기
        
        # 목표 지점 도달하면 거리 반환
        if cx == n - 1 and cy == m - 1:
            return maps[cx][cy]

        # 상하좌우 탐색
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            
            # 맵 범위 안에 있고, 벽이 아니며 방문하지 않은 경우 이동 가능
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[cx][cy] + 1  # 거리 갱신
                queue.append((nx, ny))  # 큐에 추가하여 탐색 계속 진행
                
    return -1  # 도착할 수 없는 경우
