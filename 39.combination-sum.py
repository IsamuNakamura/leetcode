#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(current: list, left: int, idx:int):
            if left == 0:
                ans.append(current+[])
                return
            for i in range(idx, len(candidates)):
                if left - candidates[i] >= 0:
                    current.append(candidates[i])
                    dfs(current, left-candidates[i], i)
                    current.pop()
        dfs([], target, 0)
        return ans


# @lc code=end
