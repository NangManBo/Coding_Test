test = int(input())

for t in range(test) :
    n = int(input())

    arr = list(map(int, input().split()))
    anw = []

    for i in range(0,7) :
        count = 0 # 총 다닌 일수
        day = 0 # 목표 일수
        sub = 0 # 총 다닌 일수에서 첫 주에 안간거 뺄 거
        
        while n > day :
            count += 1
            if i == 7 : i = 0

            if (arr[i] == 1 ) :
                day += 1 
            i += 1
        anw.append(count)
        
    print(f'#{t+1} {min(anw)}')