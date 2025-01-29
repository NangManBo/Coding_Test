def dfs(n,m,start,answer) :
    if(len(answer) == m) :
        print(" ".join(map(str,answer)))
        return
    
    for i in range(start, n + 1) :
        dfs(n,m,i + 1,answer + [i])
            
n, m = map(int,input().split())
visited = [False for _ in range(n+1)] 
dfs(n,m,1,[])