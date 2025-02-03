def solution(quiz):
    answer = []
    
    for i in range(len(quiz)) :
        quiz[i] = quiz[i].replace('=','==')
        if eval(quiz[i]) :
            answer.append("O")
        else :
            answer.append("X")
    return answer