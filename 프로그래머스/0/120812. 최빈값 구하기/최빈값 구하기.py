def solution(array):
    answer = 0
    n_arr = []
    c_arr=[]
    num = set(array)
    temp = 0
    count = 0
    for i in num :
        # 숫자, 빈도 수
        n_arr.append(i)
        c_arr.append(array.count(i))
        
    for i in range(len(c_arr)) :
        if(c_arr[i] > temp) :   # 이전 빈도 수와 현재 빈도수 비교
            answer = n_arr[i]   # 숫자 저장
            count = c_arr[i]    # 빈도 수 저장
            temp = count        # 이전 빈도 수 저장
            
    if(c_arr.count(count) > 1) :
        answer = -1
        
    return answer