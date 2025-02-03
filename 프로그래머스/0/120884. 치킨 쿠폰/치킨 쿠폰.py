def solution(chicken):
    answer = 0
    num = chicken
    while num >= 10 :
        # 100 -> 10
        answer += int(num / 10)
        # 1081 -> 109 -> 19 -> 10
        num = int(num / 10) + int(num % 10)
        
    return answer