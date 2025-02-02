from itertools import permutations

def solution(dots):
    answer = 0
    
    ex = [0,1,2,3]
    arr = list(permutations(ex,4))
    line1_x, line1_y , line2_x, line2_y = 0, 0, 0, 0
    # 0 1 2 3
    for i in arr :
        # 점 2개 먼저 비교
        line1_x = dots[i[0]][0] - dots[i[1]][0]
        line1_y = dots[i[0]][1] - dots[i[1]][1]
        # 그 다음 점 2개 비교
        line2_x = dots[i[2]][0] - dots[i[3]][0]
        line2_y = dots[i[2]][1] - dots[i[3]][1]
        
        if(float(line1_y / line1_x) == float(line2_y / line2_x)) :
            answer = 1
            break
        
    return answer