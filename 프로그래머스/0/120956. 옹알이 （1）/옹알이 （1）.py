def solution(babbling):
    answer = 0
    
    possible_word = [ "aya", "ye", "woo", "ma" ]
    for word in babbling :
        temp = word
        
        for w in possible_word :
            temp = temp.replace(w," ")

        if temp.strip() == "" :
            answer += 1
            
    return answer