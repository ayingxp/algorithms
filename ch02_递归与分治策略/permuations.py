# 使用递归(回溯)求解全排列问题

def perm(lst, start, end):
    """
    对lst从start 到　end　区间内的元素进行全排列
    :param lst:
    :param start:
    :param end:
    :return:
    """

    if start == end:
        print(lst[:])

    else:
        for i in range(start, end):
            lst[start], lst[i] = lst[i], lst[start]
            perm(lst, start + 1, end)  # 递归
            lst[start], lst[i] = lst[i], lst[start]  # 回溯



if __name__ == "__main__":
    lst = list("ABC")

    perm(lst, 0, len(lst))


