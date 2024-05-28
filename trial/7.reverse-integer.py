#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x < - 2 ** 31 or 2 ** 31 -1 < x:
            return 0
        x_char = str(x)
        is_negative = False

        if x_char[0] == '-':
            x_char = x_char[1:]
            is_negative = True

        x_reverse = x_char[::-1]

        if is_negative:
            x_reverse = '-' + x_reverse
        x_reverse = int(x_reverse)

        if x_reverse < - 2 ** 31 or 2 ** 31 -1 < x_reverse:
            return 0
        return x_reverse


# @lc code=end
