def solution(polynomial):
    answer = ''
    arr = polynomial.split()
    x = 0
    num = 0
    for word in arr :
        if("x" in word) :
            if(word == "x") :
                x += 1
            else :
                word = word.replace('x','')
                x += int(word)
        elif(word.isdigit()) :
            num += int(word)
    
    if x != 0 and num != 0:
        if(x == 1) :
            answer =f'x + {num}'
        else :
            answer = f'{x}x + {num}'
    elif x :
        if(x == 1) :
            answer =f'x'
        else :
            answer = f'{x}x'
    else :
        answer = f'{num}'
        
    return answer