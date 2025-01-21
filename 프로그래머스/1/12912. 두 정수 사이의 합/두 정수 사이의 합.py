def solution(a, b):
    
    answer = 0
    
    if(a > b) :
        n = b
        m = a
    if(a == b) :
        n = a
        m = a
    if(a < b) :
        n = a
        m = b
        
    for i in range(n, m+1) :
        answer += i
    return answer