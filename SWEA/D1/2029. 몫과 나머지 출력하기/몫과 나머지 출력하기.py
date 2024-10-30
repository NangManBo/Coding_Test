n = int(input())

for i in range(1, n+1) :
    num = input().split()
    print(f"#{i} {int(int(num[0]) / int(num[1]))} {int(num[0]) % int(num[1])}")
   