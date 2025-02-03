def solution(lines):
    overlap = set()

    # 두 선분씩 비교하여 겹치는 구간을 찾음
    for i in range(2):
        for j in range(i + 1, 3):
            start = max(lines[i][0], lines[j][0])  # 겹치는 시작점
            end = min(lines[i][1], lines[j][1])    # 겹치는 끝점
            
            if( start < end ) :
                overlap.update(range(start,end))
            
    return len(overlap)  # 겹치는 좌표 개수 반환
