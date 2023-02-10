#
# @lc app=leetcode id=1313 lang=python3
#
# [1313] Decompress Run-Length Encoded List
#

# @lc code=start
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        freqs = [nums[i] for i in range(len(nums)) if i % 2 == 0]
        vals = [nums[i] for i in range(len(nums)) if i % 2 != 0]

        ans = []
        for freq, val in zip(freqs, vals):
            ans += [val]*freq
        return ans


# @lc code=end
