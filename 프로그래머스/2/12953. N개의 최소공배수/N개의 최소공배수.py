import math

def lcm(a, b):
    print(math.gcd(a, b))
    return (a * b) // math.gcd(a, b)  # 최소공배수 공식 사용

def solution(arr):
    answer = arr[0]  # 첫 번째 원소를 기준으로 시작
    for num in arr[1:]:  # 나머지 숫자들과 최소공배수 계산
        answer = lcm(answer, num)
    return answer
