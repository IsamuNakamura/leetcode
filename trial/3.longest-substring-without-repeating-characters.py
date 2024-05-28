#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
from collections import defaultdict
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        max_len = 0
        start = 0
        slider = 0
        strLength = len(s)

        while start < strLength and slider < strLength:
            if s[slider] not in window:
                window.add(s[slider])
                slider += 1
                max_len = max(len(window), max_len)
            else:
                window.discard(s[start]) # 無くてもエラーにならない
                start += 1

        return max_len


# @lc code=end

s = Solution
# print(s.lengthOfLongestSubstring(s, "aaa"))
print(s.lengthOfLongestSubstring(s, " "))
