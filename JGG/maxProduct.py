class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_value = 1
        min_value = 1
        max_res = -float("inf")
        for index, num in enumerate(nums):
            if num < 0:
                max_value, min_value = min_value, max_value
            max_value = max(max_value*num, num)
            min_value = min(min_value*num, num)
            max_res = max(max_value, max_res)

        return max_res
# 动态规划的思想
# 1 如果全是正数，则直接相乘最大
# 2 当遇到负数时，之前的最大值乘负数变成最小值，之前的最小值乘负数变成当前的最大值
# 3 比较最大值和最小值和当前值的大小关系，更新最大值和最小值（实际更新了子序列的起始值）