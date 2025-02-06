def solution(s):
    answer = ''
    arr = list(map(str,s))
    arr.sort(reverse=True)
    print(arr)
    answer = ''.join(arr)
    return answer