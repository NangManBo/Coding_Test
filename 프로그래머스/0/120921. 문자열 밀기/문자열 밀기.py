def solution(A, B):
    answer = 0
    temp = A
    l = len(list(map(str,A)))
    for i in range(l) :
        if(temp == B) :
            return answer
        t = temp[-1]
        temp = t + temp[0:len(A)-1]
        print(temp)
        answer +=1
    
    if(answer == l) :
        answer = -1
    return answer