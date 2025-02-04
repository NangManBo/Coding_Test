from itertools import permutations

def solution(numbers):
    answer = ''
    num = [str(i) for i in numbers] 
    num.sort(key=lambda x: x*3, reverse=True)
    answer = int(''.join(num))
    
    return str(answer)