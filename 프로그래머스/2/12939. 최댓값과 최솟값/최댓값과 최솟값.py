def solution(s):
    answer = ''
    
    arr = list(map(int, s.split()))
    
    n = min(arr)
    m = max(arr)
    
    answer = str(n) + " "+ str(m)
    return answer