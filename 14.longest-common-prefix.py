#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        elif len(strs) == 1:
            return strs[0]

        strs.sort()
        common_prefix = ""

        for i in range(len(strs[0])):
            if strs[0][i] == strs[-1][i]:
                common_prefix += strs[0][i]
            else:
                break
        return common_prefix


# @lc code=end
