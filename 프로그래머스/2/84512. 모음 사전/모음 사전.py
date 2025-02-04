from itertools import product

def solution(word):
    answer = 0
    arr = ['A', 'E', 'I', 'O', 'U']
    result = [''.join(p) for i in range(1, 6) for p in product(arr, repeat = i) ]
    result.sort()
    answer = result.index(word) + 1
    
    
    return answer