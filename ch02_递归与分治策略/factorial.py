# 递归实现阶乘

"""
         1 , n = 0
f(n) = {
         n(n-1) , n >= 1
"""


def factorial(n):
    assert n >= 0, "n不能小于0"

    if n == 0:  # 递归终止条件
        return 1
    else:  # 递归
        return n * factorial(n -1)


def factorial2(n):
    assert n >= 0, "n不能小于0"

    if n == 0:  # 递归终止条件
        res = 1
    else:  # 递归
        res = n * factorial(n -1)

    return res

if __name__ == "__main__":
    n = 5
    res = factorial2(n)
    print(res)