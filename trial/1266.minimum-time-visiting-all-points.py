#
# @lc app=leetcode id=1266 lang=python3
#
# [1266] Minimum Time Visiting All Points
#

# @lc code=start
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # ans = 0
        # for i in range(1, len(points), 1):
        #     x = abs(points[i][0] - points[i-1][0])
        #     y = abs(points[i][1] - points[i-1][1])
        #     while x > 0 or y > 0:
        #         x -=1
        #         y -=1
        #         ans +=1
        # return ans
        sec = 0
        x1,y1 = points.pop()
        while points:
            x2,y2 = points.pop()
            sec += max(abs(x2-x1),abs(y2-y1))
            x1,y1 = x2,y2
        return sec


# @lc code=end
