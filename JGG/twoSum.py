# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for i in range(len(nums)):
#             j = i+1
#             while( j < len(nums)):
#                 if target == nums[i] +nums[j]:
#                     return [i,j]
#                 else:
#                     j+=1

# 6000ms  5%

# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for index, value in enumerate(nums):
#             if target - value in nums[index+1:]:
#                 return [index, nums[index+1:].index(target - value) + index+1]      
# 688ms 48.18%

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}

        for index, value in enumerate(nums):

            for i, num in enumerate(nums):
                if num in num_dict:
                    return [num_dict[num], i]
                else:
                    num_dict[target- num] = i
    # 44ms 77.07%



   #热身热身！ 找找使用字典 hash的感觉