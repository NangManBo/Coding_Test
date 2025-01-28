def dfs(n, m, answer, visited):
    # 종료 조건: 길이가 m인 수열을 완성하면 출력
    if len(answer) == m:
        print(" ".join(map(str, answer)))
        return
    
    # 1부터 n까지 숫자 탐색
    for i in range(1, n + 1):
        if not visited[i]:  # 방문하지 않은 숫자라면
            visited[i] = True  # 숫자를 사용
            dfs(n, m, answer + [i], visited)  # 다음 단계로 이동
            visited[i] = False  # 백트래킹

# 입력 받기
n, m = map(int, input().split())
visited = [False] * (n + 1)  # 방문 여부를 저장하는 배열 (1부터 사용)
dfs(n, m, [], visited)
