def solution(s):
    answer = True
    for i in s :
        if(len(s) == 4 or len(s) == 6) :
            if(i.isalpha()) :
                answer = False
        else :
            answer = False
    return answer