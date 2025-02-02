def solution(numbers):
    answer = numbers
    
    for i in range(0,len(numbers)) :
        answer[i] = answer[i] * 2
    return answer