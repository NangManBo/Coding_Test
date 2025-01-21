def solution(x, n):
    answer = [0 for i in range(n)]
    
    for i in range(1, n + 1) :
        answer[i - 1] = i * x 
    return answer