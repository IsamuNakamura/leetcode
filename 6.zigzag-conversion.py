#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # if numRows == 1 or numRows >= len(s):
        if numRows == 1:
            return s
        ans = ['']*numRows
        row, step = 0, 0
        for w in s:
            ans[row] += w
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step
        return ''.join(ans)




# @lc code=end
