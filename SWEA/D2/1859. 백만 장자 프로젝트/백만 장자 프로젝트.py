n1 = int(input())

for i in range(1, n1+1) :
    anw = 0
    n2 = int(input())
    arr = list(map(int, input().split()))

    max = 0
    for j in range(n2-1, -1, -1):
        if max < arr[j]:
            max = arr[j]
        else :
            anw += max - arr[j]

    print(f"#{i} {anw}")