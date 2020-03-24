# 整数划分问题
# 使用递归求解整数划分问题

"""
n为给定的正整数, 将n分解为k个正整数的和:
n = n1 + n2 + n3 + n4 + ... + nk, (n1 >= n2 >= n3 >= n4 ... >= nk)
"""

results = []

def num_divide(n):
    if n <= 0:
        return  results[:]
    else:
        for k in range(n, -1, -1):
            results.append(k)
            if n - k > 0:
                num_divide(n-k)

"""
在正整数ｎ的所有不同划分中，将最大加数n1不大于m的划分数记做q(n,m)，则:

1. q(n, 1) = 1, n >= 1, 此时　n = 1 + 1 + 1 + ... + 1

2. q(n, m) = q(n, n), m >= n, 此时最大加数 n1 实际上不能大于n, 因此 q(1, m) = 1

3. q(n, n) = 1 + q(n, n-1), 此时 正整数ｎ的划分由　n1 = n 的划分和　n1 <= n -1 的划分组成

4. q(n, m) = q(n, m-1) + q(n-m, m) , n > m > 1，　此时，正整数n的最大加数n1不大于m的划分由 n1 = m的划分和
    n1 <= m -1 的划分组成
    
例子:
6;
5+1;
4+2,4+1+1;
3+3,3+2+1,3+1+1+1;
2+2+2,2+2+1+1,2+1+1+1+1;
1+1+1+1+1+1;
"""

def q(n,m):
    if n < 1 or m < 1:
        return 0
    if n == 1 or m == 1:
        return 1
    if n < m:
        return q(n, n)
    if n == m:
        return q(n, m-1) + 1
    return q(n, m-1) + q(n-m, m)

if __name__ == "__main__":
    n = 10
    res = q(n, n)
    print(res)
