def dfs(idx, score, kcal):
    global answer
    if(kcal > limit):
        return
    if(answer < score):
        answer = score
    if(idx == test):
        return
    a,b = arr[idx]

    dfs(idx+1, score+a, kcal+b)
    dfs(idx+1, score, kcal)
 

 
n = int(input())
for i in range(1,n+1):
    test,limit = map(int,input().split())
 
    arr = [list(map(int, input().split())) for _ in range(test)]
    answer = 0
    dfs(0,0,0)
    print(f"#{i} {answer}")