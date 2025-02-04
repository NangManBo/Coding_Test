def solution(citations):
    l = len(citations)
    result = 0
    citations.sort(reverse=True)
    for idx, num in enumerate(citations, start = 1) :
        # idx는 현재 논문 위치 (자신보다 높거나 같은 인용의 수를 가진 논문의 수)
        # num은 현재 인용된 수 
        result = max(result, min(num, idx))
        
    return result