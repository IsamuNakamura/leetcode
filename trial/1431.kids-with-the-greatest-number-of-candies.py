#
# @lc app=leetcode id=1431 lang=python3
#
# [1431] Kids With the Greatest Number of Candies
#

# @lc code=start
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_num = max(candies)
        return [ candy + extraCandies >= max_num for candy in candies]

        ans = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max(candies):
                ans.append(True)
            else:
                ans.append(False)
        return ans
# @lc code=end
