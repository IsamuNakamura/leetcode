#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n]*m
        # dp = [[0 for i in range(n)] for i in range(m)]
        for row in range(m):
            for col in range(n):
                if row == 0 or col == 0:
                    dp[row][col] = 1
                else:
                    dp[row][col] = dp[row-1][col] + dp[row][col-1]
        return dp[m-1][n-1]

# @lc code=end
