#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
        if num in hash:
            return [hash[num], i]
        else:
            hash[diff] = i

# @lc code=end

