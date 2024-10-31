t = int(input())

arr = [str(i) for i in range(1, t+1)]

result = [0 for k in range(len(arr))]

for j in range(1, len(arr)+1) :
    chr = ''
    count = 0
    count += arr[j-1].count('3')
    count += arr[j-1].count('6')
    count += arr[j-1].count('9')

    if(count == 1) :
        chr = '-'
    elif (count == 2) :
        chr ='--'
    elif (count == 3) :
        chr = '---'
    else : 
         chr = j

    result[j - 1] = chr

for k in range(len(arr)) :
    print(result[k], end = " ")
    
    