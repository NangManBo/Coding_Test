def longest_increasing_subsequence(arr, n):
    dp = [1] * n  # 모든 요소를 포함하는 길이는 최소 1

    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# 입력 처리 및 실행
test_case = int(input())

for t in range(1, test_case + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = longest_increasing_subsequence(arr, N)
    print(f'#{t} {result}')
