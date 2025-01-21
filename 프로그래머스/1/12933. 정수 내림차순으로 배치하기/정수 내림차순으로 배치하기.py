def solution(n):
    answer = 0
    
    arr = list(map(str, str(n)))
    
    
    answer = int(''.join(sorted(arr, reverse=True)))
    
    
    return answer