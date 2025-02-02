def solution(my_string):
    answer = ''
    word = ['a', 'e', 'i', 'o', 'u']
    
    for i in word :
        my_string = my_string.replace(i,'')
    
    answer = my_string
    
    return answer