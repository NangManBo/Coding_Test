def solution(bandage, health, attacks):
    answer = health
    # bandage[0] = t (시전시간) [1] = x 초당 회복량 [2] = y 추가 회복량인데 t만큼 회복을 진행했다면 ㄱㄱ
    # health = 최대 체력
    
    # 우선 계속 피를 채운다
    # 그러다가 맞을 때는 피 회복 x
    
    # 조건
    # for문 시작할 때 무조건 피 검사 해서 0 보다 작으면 -1 1이상일 경우 진행 그리고 최대체력을 넘어갔다면 다시 health
    # 1. 피 0이 되면 끝
        # 1-1. 맞은 후 끝 나면 바로 break로 탈출
        # 1-2. i를 설정해서 attacks[i][0] 에 있는 값일 때만 맞도록 설정
        # 1-3. 맞고 이제 다시 for문 j = 2로 돌아왔을 경우 answer 값 확인 해서 answer == 0이면 break
    # 2. 아닐 때는 피 회복
        # 2-1. 피가 최대체력을 넘어가있는 상태면 다시 최대체력으로 바꿀 것
        # 2-2. bandage[2]의 카운터만큼 하면 체력 추가로 더하기
        
    l = len(attacks)
    m = attacks[l-1][0]
    count = 0
    i = 0
    
    for j in range(1, m + 1) :
        if(answer > health) :
            answer = health
        if (answer <= 0) :
            answer = -1
            break
        elif (answer > 0) :
            if(j == attacks[i][0]) :
                answer -= attacks[i][1]
                i += 1
                count = 0
            elif (j != attacks[i][0]) :
                if(answer < health) :
                    answer += bandage[1]
                    count += 1
                    if(count == bandage[0]) :
                        answer += bandage[2]
                        count = 0
        
            
    if(answer <= 0) :
        answer = -1
            
    return answer