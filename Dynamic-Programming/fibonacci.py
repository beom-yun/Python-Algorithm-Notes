# 다이나믹 프로그래밍(Dynamic Programming)
# 큰 문제를 작게 나누고, 같은 문제라면 한 번씩만 풀어 문제를 표율적으로 해결하는 알고리즘 기법
# 주로 점화식으로 나타내어 해결한다
#
# 퀵 정렬의 경우도 큰 문제를 작게 나누어 해결하지만(분할정복 Divide and conquer),
# 문제들이 서로 영향을 미치지 않으므로 다이나믹 프로그래밍이 아니다.


# 피보나치 수열(재귀적, 탑다운 방식 Top-Down)
# 한 번 계산된 결과를 메모이제이션(일시적으로 저장)
# 메모이제이션 기법은 탑다운 방식에서만 국한되어 사용하는 표현이다
memoization_list = [0] * 100


def recursive_fibo(x):
    if x == 1 or x == 2:                # 종료 조건(1 또는 2일 때)
        return 1
    if memoization_list[x] != 0:        # 한 번 계산한 적이 있을 때
        return memoization_list[x]
    memoization_list[x] = recursive_fibo(x - 1) + recursive_fibo(x - 2)
    return memoization_list[x]


print(recursive_fibo(99))


# 피보나치 수열(반복적, 보텀업 방식 Bottom-Up)
# 다이나믹 프로그래밍의 전형적인 형태는 보텀업 방식이다.
dp_table = [0] * 100

dp_table[1] = 1
dp_table[2] = 1
n = 99

for i in range(3, n + 1):
    dp_table[i] = dp_table[i - 1] + dp_table[i - 2]

print(dp_table[99])


# 가능하다면 재귀 함수를 이용하는 탑다운 방식보다는 보텀업 방식으로 구현하도록 하자
