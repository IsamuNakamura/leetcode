#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# import itertools
# @lc code=start
class Solution:
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     return list(itertools.permutations(nums))
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []
        self.dfs(self, nums, [], ans)
        return ans

    def dfs(self, start: list[int], end: list, ans: list):
        if len(start) == 0:
            ans.append(end)
            print("append")
        else:
            for i in range(len(start)):
                print("i: %d" % i)
                print(start[:i] + start[i+1:])
                print(end + [start[i]])
                print("-----")
                self.dfs(self, start[:i] + start[i+1:], end + [start[i]], ans)




# @lc code=end

s = Solution
s.permute(s, [1,2,3])
