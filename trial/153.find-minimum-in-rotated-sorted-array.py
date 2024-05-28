#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1

        while low < high:
            mid = (high + low) // 2

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]

# @lc code=end
