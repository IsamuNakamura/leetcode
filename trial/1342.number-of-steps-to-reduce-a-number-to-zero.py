#
# @lc app=leetcode id=1342 lang=python3
#
# [1342] Number of Steps to Reduce a Number to Zero
#

# @lc code=start
class Solution:
    def numberOfSteps(self, num: int) -> int:
        ans = 0
        while num > 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            ans += 1
        return ans

# @lc code=end
