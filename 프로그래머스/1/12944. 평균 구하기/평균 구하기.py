def solution(arr):
    
    answer = 0
    
    l = len(arr)
    for i in range(l) :
        answer += arr[i]
    
    answer = float(answer / l)
    return answer