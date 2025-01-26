def solution(s):
    answer = []
    count = 0
    delete_zero = 0
    
    arr = list(map(int,s))

    while(1) :
        # 0 세는 곳
        delete_zero += arr.count(0)
        # 횟수 세는 곳
        count += 1
        
        # 배열 길이에서 0 포함 빼기 그럼 1만 남음
        l = len(arr) - arr.count(0)
        # 그 길이만큼 1에 대한 배열 생성 후 join으로 합치기
        x = [str(1) for i in range(l)]
        x_int = ''.join(x)
        
        if(int(x_int) == 1) :
            answer.append(count)
            answer.append(delete_zero)
            break
        # 아까 구한 1의 길이로 다시 2진 만들기
        arr = list(map(int,(bin(l)[2:])))
        
    return answer