#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = (low + high) // 2

            if target == nums[mid]:
                print("mid")

                return mid
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        print("return")
        return low

# @lc code=end

s = Solution()
print(s.searchInsert([1,3,5,6], 2))
print(s.searchInsert([1,3,5,6], 7))
print(s.searchInsert([1,3,5,6], 0))
