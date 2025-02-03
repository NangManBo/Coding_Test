def solution(num, total):
    answer = []
    
    # num이 홀수 일 경우
    if(num % 2 != 0) :
        if (total % num == 0) :
            a = int(total / num)
            b = int(num / 2)
            for i in range(a - b, a + b + 1) :
                answer.append(i)
    
    # num이 짝수 일 경우
    elif(num % 2 == 0) :
        a = int(total / num)
        b = int(num / 2) - 1
        for i in range(a - b, a + b + 2) :
            answer.append(i)
                
    return answer