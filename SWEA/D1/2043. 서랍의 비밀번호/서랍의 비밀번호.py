n = input().split()

result = 0
anw = int(n[1])

while 1 :
    result += 1
    if(int(n[0]) == anw) :
        break
    anw += 1
        
print(result)