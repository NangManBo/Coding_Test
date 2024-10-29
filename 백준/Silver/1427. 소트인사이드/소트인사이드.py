num = input()

a= []
def main(num) -> int:
    
    for i in str(num):
        a.append(i)

    a.sort(reverse=True)
    answer = 0

    for i in range(len(a)):
        answer += int(a[i]) * 10 ** (len(a) -i -1)

    return answer; 
   

# 실행
print(main(num))

