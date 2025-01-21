def solution(n):
    answer = 0

    l = len(str(n))
    m = n
    
    for i in range(1, l + 1) :
        answer += m % 10
        m = int(m / 10)
        
    return answer