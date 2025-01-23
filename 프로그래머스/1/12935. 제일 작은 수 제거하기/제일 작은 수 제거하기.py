def solution(arr):
    answer = []
    
    arr.remove(min(arr))
    
    if(len(arr) > 1) :
        answer = arr
    else :
        answer.append(-1)
    return answer