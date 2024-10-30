t = int(input())

for test_case in range(1, t + 1):
    num = int(input())
    arr = [[0] * num for _ in range(num)]  # num x num 크기의 2차원 배열 생성

    # 방향 설정 (우, 하, 좌, 상)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_index = 0  # 현재 방향 인덱스
    x, y = 0, 0  # 시작 위치
    current_value = 1  # 시작 값

    while current_value <= num * num:
        arr[x][y] = current_value  # 현재 위치에 값 할당
        current_value += 1

        # 다음 위치 계산
        next_x = x + directions[direction_index][0]
        next_y = y + directions[direction_index][1]

        # 배열 범위를 벗어나거나 이미 값이 채워져 있는 경우 방향 변경
        if next_x < 0 or next_x >= num or next_y < 0 or next_y >= num or arr[next_x][next_y] != 0:
            direction_index = (direction_index + 1) % 4  # 방향을 시계방향으로 전환
            next_x = x + directions[direction_index][0]
            next_y = y + directions[direction_index][1]

        # 위치 업데이트
        x, y = next_x, next_y

    # 출력
    print(f'#{test_case}')
    for row in arr:
        print(" ".join(map(str, row)))
