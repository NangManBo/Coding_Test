def dfs(index, current_value, num, operators, last, result):
    # 종료 조건: 모든 연산자를 사용한 경우
    if index == last:
        result.append(current_value)
        return

    # 연산자 (덧셈, 뺄셈, 곱셈, 나눗셈) 순서대로 적용
    for i in range(4):
        if operators[i] > 0:  # 연산자가 남아 있는 경우에만 진행
            operators[i] -= 1  # 해당 연산자 사용
            
            # 새로운 값 계산
            if i == 0:  # 덧셈
                new_value = current_value + num[index]
            elif i == 1:  # 뺄셈
                new_value = current_value - num[index]
            elif i == 2:  # 곱셈
                new_value = current_value * num[index]
            elif i == 3:  # 나눗셈 (C++ 스타일)
                if current_value < 0:
                    new_value = -(-current_value // num[index])
                else:
                    new_value = current_value // num[index]

            # DFS 호출 (다음 숫자로 이동)
            dfs(index + 1, new_value, num, operators, last, result)

            # 백트래킹 (연산자 복구)
            operators[i] += 1


# 입력 받기
n = int(input())
num = list(map(int, input().split()))
operators = list(map(int, input().split()))  # [덧셈 개수, 뺄셈 개수, 곱셈 개수, 나눗셈 개수]

# DFS 수행
result = []
dfs(1, num[0], num, operators, n, result)

# 결과 출력
print(max(result))  # 최댓값
print(min(result))  # 최솟값
