test = int(input())

for t in range(test) :
    T, N = map(str, input().split())
    a,b,c,d,e,f,g,h,j,k = [],[],[],[],[],[],[],[],[],[]
 
    arr = list(map(str, input().split()))
    anw = []

    for i in range(int(N)) :
        if(arr[i] == 'ZRO') :
            a.append(arr[i])
        elif(arr[i] == 'ONE') :
            b.append(arr[i])
        elif(arr[i] == 'TWO') :
            c.append(arr[i])
        elif(arr[i] == 'THR') :
            d.append(arr[i])
        elif(arr[i] == 'FOR') :
            e.append(arr[i])
        elif(arr[i] == 'FIV') :
            f.append(arr[i])
        elif(arr[i] == 'SIX') :
            g.append(arr[i])
        elif(arr[i] == 'SVN') :
            h.append(arr[i])
        elif(arr[i] == 'EGT') :
            j.append(arr[i])
        elif(arr[i] == 'NIN') :
            k.append(arr[i])

    anw.append(a)
    anw.append(b)
    anw.append(c)
    anw.append(d)
    anw.append(e)
    anw.append(f)
    anw.append(g)
    anw.append(h)
    anw.append(j)
    anw.append(k)

    print(f'#{t+1}')
    for k in range(10) :
        if(anw[k] != []) :
            for l in range(len(anw[k])) :
                print(anw[k][l], end=" ")