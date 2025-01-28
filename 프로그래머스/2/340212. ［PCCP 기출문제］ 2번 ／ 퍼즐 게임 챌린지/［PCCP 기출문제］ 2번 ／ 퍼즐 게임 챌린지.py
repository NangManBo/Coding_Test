def solution(diffs, times, limit):
    def can_complete(level):
        total_time = 0
        time_prev = 0  # 이전 퍼즐의 소요 시간
        
        for diff, time_cur in zip(diffs, times):
            if diff <= level:
                total_time += time_cur
            else:
                mistakes = diff - level
                total_time += mistakes * (time_cur + time_prev) + time_cur
            
            # 제한 시간을 초과하면 False
            if total_time > limit:
                return False
            
            time_prev = time_cur  # 현재 퍼즐의 시간을 다음 퍼즐에 전달
        
        return True

    # 이진 탐색 범위 설정
    left, right = 1, max(diffs)  # 숙련도는 1 이상이며, 최대 난이도 이하
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        if can_complete(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer
