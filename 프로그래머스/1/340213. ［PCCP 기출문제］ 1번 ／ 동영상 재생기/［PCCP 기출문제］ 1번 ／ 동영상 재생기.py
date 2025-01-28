def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    last = [0 for i in range(5)]
    # 배열에 담아서 2번쨰 자리 빼고 0134만 합치기
    arr = [video_len,pos,op_start,op_end]
    result = [0 for i in range(4)]
    
    for i in range(4) :
        result[i] = list(map(str, arr[i]))
        result[i].remove(result[i][2])
        result[i] = int(''.join(result[i]))
        
    # 현재 위치 pos
    current = result[1]
    # 첫 시작이 오프닝 안에 있을 경우
    if(result[2] < current < result[3]) :
        current = result[3]
            
    for word in commands :
        if(word == 'next') :
            current += 10
            # 숫자 값이 60분을 넘어갈때 ex) 1372 -> 1412
            if (current % 100 >= 60) :
                current += 40
        elif(word == 'prev') :
            current -= 10
            # 숫자 값이 ex) 1407 -> 1397 97이니까 57로 만들기
            if (current % 100 >= 60) :
                current -= 40
        
        # 현재 시간 기준 00:00보다 작을 때 
        if(current <= 0) :
            current = 0
        # 현재 시간이 총 영상 시간을 넘어갈 때 
        # 1372였으면 안걸리지만 바꾼 후에 1412가 되므로 
        # 1400 영상보다 커짐 그럼 다시 1400으로 돌아오게끔
        if(current >= result[0]) :
            current = result[0]
            
        # 이동한 위치가 오프닝 안
        if(result[2] <= current <= result[3]) :
            current = result[3]
            
    # 100기준으로 앞뒤 짤라서 내보내기
    minutes = int(current / 100)
    seconds = current % 100
        
    answer = str(f"{minutes:02}:{seconds:02}")
    
    return answer