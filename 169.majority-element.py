#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
import collections
# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        return counter.most_common()[0][0]

        hashMap = {}
        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        return max(hashMap.items(), key = lambda x:x[1])[0]

# @lc code=end
