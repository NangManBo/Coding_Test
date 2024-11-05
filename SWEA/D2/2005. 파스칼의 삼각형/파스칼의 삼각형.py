t = int(input())

for test in range(1, t + 1) :
   
    num = int(input())
    print(f"#{test}")

    for i in range(num) :
        x = 11 ** i
        print(" ".join(str(x)))