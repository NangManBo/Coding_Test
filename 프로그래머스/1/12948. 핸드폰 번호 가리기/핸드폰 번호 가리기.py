def solution(phone_number):
    answer = ''
    
    l = len(phone_number)
    
    arr = list(map(str, str(phone_number)))
    
    for i in range(l-4) :
        arr[i] = '*'
    answer = ''.join(arr)
        
    return answer