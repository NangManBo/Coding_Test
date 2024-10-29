n = input()


def main(n) -> int:

    m = list(map(int, n))
    result = 0
    for j in range(len(m)) :
        result += m[j] 
            
    print(f'{result}')
    
main(n)
