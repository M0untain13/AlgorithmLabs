import math


def catalan_recursive(n):
    if n <= 1:
        return 1
    res = 0
    for i in range(n):
        res += catalan_recursive(i) * catalan_recursive(n - 1 - i)
    return res

def catalan_dp(n):
    if n <= 1:
        return 1
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - 1 - j]
    return dp[n]


def catalan_binom(n):
    return math.comb(2 * n, n) // (n + 1)

n = 16
def example_recursive():
    global n
    C = catalan_recursive(n)
    print(f"\tПри n = {n}, число Каталана равно {C}")


def example_dp():
    global n
    C = catalan_dp(n)
    print(f"\tПри n = {n}, число Каталана равно {C}")


def example_binom():
    global n
    C = catalan_binom(n)
    print(f"\tПри n = {n}, число Каталана равно {C}")
