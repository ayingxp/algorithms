"""
全排列问题，使用回溯法
"""

def permute(nums):
    def backtrack(first=0):
        if first == n:
            output.append(nums[:])
        for i in range(first, n):
            nums[first], nums[i] = nums[i], nums[first]
            backtrack(first + 1)
            # 回溯
            nums[first], nums[i] = nums[i], nums[first]

    n = len(nums)
    output = []
    backtrack()
    return output


if __name__ == "__main__":
    nums = [1,2,3]

    output = permute(nums)
    print("")
    print("output:\n")
    print(output)
