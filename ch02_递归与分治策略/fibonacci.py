# 用递归解决非波纳契数列

"""

f(0) = 1
f(1) = 1
f(n) = f(n-1) + f(n-2)

"""

from functools import lru_cache

#@lru_cache()
def fibonacci(n):
    assert n >= 0, "n 不能小于0"

    if n in [0, 1]:  # 递归终止条件
        res = 1  # or return 1

    else:  # 递归s
        res = fibonacci(n-1) + fibonacci(n-2) # or return fibonacci(n-1) + fibonacci(n-2)
    return res


if __name__ == "__main__":
    n = 8
    res = fibonacci(n)
    print(res)

