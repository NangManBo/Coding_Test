t = int(input())

for test_case in range(1, t + 1):
    num = input()
    arr = list(map(int,input().split()))
    max = 0
    anw = 0
    for i in range(len(arr)) :
        if (arr.count(arr[i]) > max) :
            max = arr.count(arr[i])
            anw = arr[i]

    print(f"#{num} {anw}")


   
    

   
