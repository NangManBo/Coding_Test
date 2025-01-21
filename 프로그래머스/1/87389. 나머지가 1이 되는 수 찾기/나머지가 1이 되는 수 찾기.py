def solution(n):
    
    answer = n
    min = 0
    for i in range(1, n) :
        if(n % i == 1) :
            min = i
            if (answer > min) :
                answer = min
    
        
    return answer