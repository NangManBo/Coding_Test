def solution(s):
    answer = ''
    n = len(s)
    word = list(map(str, s))
    
    # 길이가 짝수면 2개 내보내기 ex) 길이 4면 1,2 -> 4/2 = 2 - 1
    if( n % 2 == 0 ) :
        answer = word[int(n/2) - 1] + word[int(n/2)]     
    # 길이 홀수 ex) 5 2를 내보내야함 
    else :
        answer = word[int(n/2)]
    
    
        
    return answer