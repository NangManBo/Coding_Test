from collections import deque

N, M = list(map(int, input().split()))

pic = [list(map(int, input().split())) for i in range(N)]
visted = [[False for _ in range(M)] for _ in range(N)]

max_num = 0
max_value = 0 

def BFS(start_x, start_y, graph, visited) :
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[start_x][start_y] = True
    
    component=[]
    queue = deque([(start_x,start_y)])
    while queue :
        x, y = queue.popleft()
        component.append((x,y))

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < N and 0 <=ny < M :
                if graph[nx][ny] and not visited[nx][ny] :
                    visited[nx][ny] = True
                    queue.append((nx,ny))

    global max_value
    if(len(component) > max_value) :
        max_value = len(component)
    return component

def solution(graph):
	# 응용 포인트1: bfs()에게 넘겨줄 visited 생성
    n, m = len(graph), len(graph[0])
    visited = [[False] * m for _ in range(n)]

	# 응용 포인트4: 모든 노드를 순회하며, 각각의 모든 연결요소 탐색
    answer = []
    for i in range(n):
        for j in range(m):
        	# 응용 포인트5: 중복되지 않도록 solution()에서 이동 조건 검사
            if graph[i][j] and not visited[i][j]:
                answer.append(BFS(i, j, graph, visited))
    global max_num
    max_num = len(answer)
    return answer

solution(pic)
print(max_num)
print(max_value)
