#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
import collections
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for str in strs:
            sortedStr = ''.join(sorted(str))
            ans[sortedStr].append(str)

        return ans.values()

# @lc code=end
