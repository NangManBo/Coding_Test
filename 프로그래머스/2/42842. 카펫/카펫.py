def solution(brown, yellow):
    answer = []
    s = brown + yellow
    
    for w in range(1, s + 1) :
        if(s % w == 0) :
            h = s // w
            
            if(w >= h) :
                if(w-2) * (h-2) == yellow :
                    answer=[w,h]    
    return answer