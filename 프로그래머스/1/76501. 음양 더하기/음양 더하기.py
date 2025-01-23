def solution(absolutes, signs):
    answer = 0
    
    answer = sum(absolutes)
    
    arr = []
    l_s = len(signs)
    
    for i in range(l_s) :
        if(signs[i] == False) :
            arr.append(i)
    
    l_a = len(arr)
    
    for k in range(l_a) :
        answer -= absolutes[arr[k]] * 2
        
    return answer