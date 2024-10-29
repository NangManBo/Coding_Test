n = input()


def main(n) -> int:

    
    for i in range(1, n+1) :
       result = 0
       number = list((map(int, input().split())))
       for j in range(0, len(number)) :
            result += number[j]

       print(f"#{i} {int(round(result / len(number)))}")

main(int(n))
