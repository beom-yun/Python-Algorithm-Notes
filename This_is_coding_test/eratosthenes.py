# 에라토스테네스의 체

def solution(n):
    num = set(range(2, n + 1))

    for i in range(2, n + 1):
        if i in num:
            num -= set(range(i * 2, n + 1, i))
    return num
