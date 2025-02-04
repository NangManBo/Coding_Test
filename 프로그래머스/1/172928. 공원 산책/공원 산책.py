def check(current, chain, w, h):
    x, y = current
    if 0 > x or x >= h or 0 > y or y >= w:  # 범위 체크
        return False
    if current in chain:  # 장애물 체크
        return False
    return True

def solution(park, routes):
    h, w = len(park), len(park[0])  # 공원의 크기 (int 변환 필요 없음)
    start = None
    chain = set()  # 집합(set) 사용으로 탐색 속도 개선

    # 1️⃣ S(출발 위치)와 X(장애물) 찾기 (enumerate 사용)
    for i, row in enumerate(park):
        for j, cell in enumerate(row):
            if cell == 'S':
                start = (i, j)  # 시작 위치 저장 (튜플)
            elif cell == 'X':
                chain.add((i, j))  # 장애물 위치 저장

    # 2️⃣ 이동 실행
    current = start  # 현재 위치 저장
    direction = {'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)}  # 이동 방향 딕셔너리

    for r in routes:
        dx, dy = direction[r[0]]  # 이동 방향 가져오기
        steps = int(r[2])  # 이동 거리
        pre = current  # 이전 위치 저장 (복사)

        for _ in range(steps):
            next_pos = (current[0] + dx, current[1] + dy)  # 다음 위치 계산
            if not check(next_pos, chain, w, h):  # 장애물 또는 범위 초과 시 복귀
                current = pre
                break
            current = next_pos  # 이동 성공 시 업데이트
    
    return list(current)  # 리스트로 변환 후 반환
