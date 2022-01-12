# 가장 긴 증가하는 부분수열(LIS, Longest Increasing Subsequence)
#
# 전형적인 다이나믹 프로그래밍 문제 아이디어
# dp[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이

array = [10, 20, 10, 30, 20, 50]
dp = [1] * len(array)               # dp테이블은 1로 초기화

# 모든 0 <= j < i 에 대하여, dp[i] = max(dp[i], d[j] + 1) if array[j] < array[i]
for i in range(1, len(array)):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print('가장 긴 증가하는 부분 수열의 길이 :', max(dp))
