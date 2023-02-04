#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
import itertools
# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(nums), -1, -1):
            ans += (self.combinations(nums, i))
        return ans
    def combinations(self, data: list, selectNum: int) -> List:
        if selectNum == 0:
            return [[]]
        elif selectNum == 1:
            return [[val] for val in data]
        else:
            results = []
            for i, val in enumerate(data):
                rest_vals = self.combinations(data[i+1:], selectNum-1) # (i+1)番目以降の要素を使えばいい
                # rest_vals = self.combinations(data[:i+1] + data[i+1:], selectNum-1) # 重複組み合わせ
                for rest_val in rest_vals:
                    result = [val] + rest_val
                    results.append(result)
            return results



# @lc code=end
