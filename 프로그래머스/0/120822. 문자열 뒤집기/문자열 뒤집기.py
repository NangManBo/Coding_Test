def solution(my_string):
    answer = list(map(str,my_string))
    print(answer)
    answer.reverse()
    answer = ''.join(answer)
    
    return answer