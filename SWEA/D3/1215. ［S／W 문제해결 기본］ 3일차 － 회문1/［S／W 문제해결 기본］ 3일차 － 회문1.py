def check(lis, num) :
    count = 0
    if(num == 1) :
        return 1
    
    for i in range(int(num/2)) :
        if(str(lis[i]) == str(lis[num-i-1])) :
            count += 1

    if(int(num / 2) == count) :
        return 1
    else :
        return 0
    


def r_cal(arr, x, y, num) :
    r_lis = []

    sum = 0

    for i in range(num):
        r_lis.append(arr[x][y + i])

    sum += check(r_lis,num)
   
    return sum

def d_cal(arr, x, y, num) :
    d_lis = []
    sum = 0

    for i in range(num):
        d_lis.append(arr[x + i][y])
   
    sum += check(d_lis,num)
    
    return sum

for t in range(1,11) :
    num = int(input())
    arr = [list(map(str, input())) for _ in range(8)]
    anw = 0

    for i in range(8) :
        for j in range(8 - num + 1) :
            anw += r_cal(arr, i, j ,num)
            anw += d_cal(arr, j, i, num)
            
    
    print(f'#{t} {anw}')       

