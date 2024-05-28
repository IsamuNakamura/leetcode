#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

import heapq
import collections

# @lc code=start
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        return [i for i, v in collections.Counter(nums).most_common(k)]
# @lc code=end

s = Solution
print(s.topKFrequent(s, [1,1,1,2,2,3], 2))
