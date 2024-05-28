#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        print(sorted_nums)

        start, end = 0, 0
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                start = i
                break
        for i in range(len(nums)-1, start, -1):
            if nums[i] != sorted_nums[i]:
                end = i
                break
        return end - start + 1 if end - start != 0 else 0

        # O(n)
        l,u = len(nums)-1, 0
        stack=[]
        for i in range(len(nums)):
            while stack and nums[stack[-1]]>nums[i]:
                l = min(l, stack.pop())
            stack.append(i)

        stack=[]
        for i in range(len(nums)-1,-1, -1):
            while stack and nums[stack[-1]]<nums[i]:
                u = max(u, stack.pop())
            stack.append(i)

        return 0 if l>=u else u-l+1



# @lc code=end
