import math

def is_prime(num) :
    if num <= 1 :
        return False
    if num in [2,3,5,7] :
        return True
    for i in range(2, int(math.sqrt(num)) + 1) :
        if(num % i == 0) :
            return False
    return True

from itertools import permutations
def solution(numbers):
    answer = set()
    arr = [list(p) for i in range(1,len(numbers)+1) for p in set(permutations(numbers,i))]
    
    for i in range(len(arr)) :
        if is_prime(int(''.join(arr[i]))) :
            answer.add(int(''.join(arr[i])))
    
    return len(answer)