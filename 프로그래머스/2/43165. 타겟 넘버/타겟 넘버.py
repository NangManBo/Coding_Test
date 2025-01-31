def dfs(index, current_sum, numbers, target):
    # 모든 숫자를 사용한 경우 (종료 조건)
    if index == len(numbers):
        return 1 if current_sum == target else 0

    # 현재 숫자를 + 또는 -로 사용하여 다음 DFS 탐색
    return dfs(index + 1, current_sum + numbers[index], numbers, target) + \
           dfs(index + 1, current_sum - numbers[index], numbers, target)


def solution(numbers, target):
    return dfs(0, 0, numbers, target)
