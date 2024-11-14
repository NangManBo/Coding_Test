test = int(input())

def cal(arr, anw, num) :
    if num == arr[2] :
        anw = arr[3] - arr[1] + 1
        return anw
    elif num < 8 :
        if num == 2 :
            anw += 28 - arr[1] + arr[3]
        else :
            if num % 2 == 0 :
                anw += (30 - arr[1] + arr[3]) 
            elif num %2 == 1 :
                anw += (31 - arr[1] + arr[3]) 
    elif num >= 8 :
        if num % 2 == 0 :
            anw += (31 - arr[1] + arr[3]) 
        elif num %2 == 1 :
            anw += (30 - arr[1] + arr[3]) 
    return anw + 1

for t in range(test) :
    arr = list(map(int, input().split()))
    anw = 0
    anw += cal(arr, anw, arr[0])

    if(arr[2] != arr[0]) :
        for i in range(1, arr[2] - arr[0]) :
            num = (arr[2] - i)
            if num < 8 :
                if num == 2 :
                    anw += 28
                else : 
                    if num % 2 == 0 :
                        anw += 30
                    elif num %2 == 1 :
                        anw += 31 
            elif num >= 8 :
                if num % 2 == 0 :
                    anw += 31
                elif num %2 == 1 :
                    anw += 30

    print(f"#{t+1} {anw}")

