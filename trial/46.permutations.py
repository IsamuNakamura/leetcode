#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# import itertools
# @lc code=start
class Solution:
    # 解法1
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     return list(itertools.permutations(nums))

    # 解法2
    # def permute(self, nums: list[int]) -> list[list[int]]:
    #     ans = []
    #     self.dfs(self, nums, [], ans)
    #     return ans

    # def dfs(self, start: list[int], end: list, ans: list):
    #     if len(start) == 0:
    #         ans.append(end)
    #         print("append")
    #     else:
    #         for i in range(len(start)):
    #             print("i: %d" % i)
    #             print(start[:i] + start[i+1:])
    #             print(end + [start[i]])
    #             print("-----")
    #             self.dfs(self, start[:i] + start[i+1:], end + [start[i]], ans)

    # 解法3
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 1:
                return [nums] # 1. 要素数1の順列を返す
        else:
            result = [] # 順列の組を保存しておくためのリスト
            for i, val in enumerate(nums): # 1. 数字の組から1つ取り出す
                rest = self.permute(nums[:i] + nums[i+1:]) # 2. 残りの数字の組から順列の組を作る
                print('rest:', rest)
                for rest_perm in rest:
                    perm = [val] + rest_perm # 3. 求まった順列の先頭に1で取り出した数字をくっつける
                    result.append(perm)
                    print('result:', result)

            return result
# @lc code=end

s = Solution
s.permute(s, [1,2,3])
