"""
给定书的页码 n，求全部页码中分别用到了多少次0,1,2,3,4,5,6,7,8,9
"""


def count_num(n):
    res = {}

    for i in range(1, n+1):
        for k in str(i):
            old_val = res.get(int(k), 0)
            res.update({int(k): old_val + 1})
    return res


def count_num_2(n):
    return 


if __name__ == '__main__':
    n = 11

    res = count_num(n)
    
    print(res)
