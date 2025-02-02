def solution(slice, n):
    answer = 0
    
    answer = int(n / slice)
    
    if(n % slice != 0) :
        answer += 1
    return answer