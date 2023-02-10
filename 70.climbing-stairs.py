#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
from functools import lru_cache
# @lc code=start
class Solution:
    @lru_cache(None) # important
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)

# @lc code=end
