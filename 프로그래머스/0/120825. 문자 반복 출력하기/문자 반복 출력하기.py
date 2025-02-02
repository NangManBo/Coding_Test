def solution(my_string, n):
    answer = []
    arr = list(map(str,my_string))
    
    print(arr)
    for i in range(len(arr)) :
        for j in range(n) :
            answer.append(arr[i])
    
    answer = ''.join(answer)
    return answer