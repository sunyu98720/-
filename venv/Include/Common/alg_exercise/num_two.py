class Solution(object):
    u"""
    给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
    你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

    """

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 暴力循环破解
        list_index = []
        s = 0
        for i, j in enumerate(nums):
            s += 1
            print("s的值为", s)
            for x in range(len(nums)):
                x = x + s if x + s < len(nums) else x
                if j + nums[x] == target:
                    list_index.append(i)
                    list_index.append(x)
                    return list_index

    def twoSum_1(self, nums, target):
        tmp = {}
        for k, v in enumerate(nums):
            if target - v in tmp:
                return [tmp[target - v], k]
            tmp[v] = k

if __name__ == '__main__':
    nums = [2, 11,7, 15]
    target = 9
    s = Solution()
    s.twoSum_1(nums, target)
