i = int(input())
arr = list(map(int,input().split()))

arr.sort()

print(arr[round(i/2)-1])