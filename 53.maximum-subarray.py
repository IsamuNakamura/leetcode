#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        current_sum = 0
        for num in nums:
            current_sum += num
            max_sum = max(max_sum, current_sum)
            current_sum = max(0, current_sum)
        return max_sum
# @lc code=end
