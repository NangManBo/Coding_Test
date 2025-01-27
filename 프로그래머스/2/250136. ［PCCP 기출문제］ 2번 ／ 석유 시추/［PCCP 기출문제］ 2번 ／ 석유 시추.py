def solution(land):
    answer = 0
    
    oil_size = {}
    
    # 우선 DFS로 크기 구하기
    n, m = len(land), len(land[0]) # n이 세로(5)  m이 가로(8)
    visited = [[False] * m for i in range(n)]
    direct = [(-1,0), (1,0), (0,1), (0,-1)]
    
    # 그리고 오일 땅에 대한 크기를 몇번 땅인지 알 수 있게 끔
    oil_arr=[[0] * m for i in range(n)] 

    # n,m의 좌표대로 0,0 부터 시작해서 끝까지 도는데 그 사이에 방문하지 않고
    # land가 1인 곳이라면 석유 크기 += 1 해주고 근처 좌표에서 또 다시 land 값이 1인거 찾아서 stack에 저장
    
    def dfs (x,y) :
        stack = [(x,y)]
        visited[x][y] = True
        oil_arr[x][y] = oil_id
        size = 1
        
        while stack :
            cx, cy = stack.pop()
            
            for dx, dy in direct :
                nx, ny = cx + dx, cy + dy
                
                if(0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False and land[nx][ny] == 1) :
                    visited[nx][ny] = True
                    stack.append([nx,ny])
                    size += 1
                    oil_arr[nx][ny] = oil_id
        return size
            
    # 크기를 구하는 방법을 알았으니 크기에 대한 땅 덩어리 번호 매기기
    oil_id = 0
    
    for i in range(n) :
        for j in range(m) :
            if(visited[i][j] == False and land[i][j] == 1) :
                oil_id += 1
                oil_size[oil_id] = dfs(i,j)
    
    # 이제 지나 가는 길에 대해 땅 덩어리가 얼마나 지나가는지 총합을 구해야함
    # 세로로 꽂을거니까 총 8개인 m
    # 최종 가장 많은 오일
    total_oil = 0
    for k in range(m) :
        visited_oil= set()
        current_oil= 0
        for l in range(n) :
            if(land[l][k] == 1) :
                # 땅이 1이면 이제 거기 위치에 맞는 땅 덩어리 번호를 찾는 거임
                w = oil_arr[l][k]
                if w not in visited_oil :
                    current_oil += oil_size[w]
                    visited_oil.add(w)
        total_oil = max(current_oil, total_oil)
    
    return total_oil