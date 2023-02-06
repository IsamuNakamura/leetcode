#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)
        while low < high:
            mid = (low + high) // 2
            current_sum_weight = 0
            required_days = 0
            for w in weights:
                if current_sum_weight + w > mid:
                    current_sum_weight = 0
                    required_days += 1
                current_sum_weight += w
            if required_days >= days:
                low = mid + 1
            else:
                high = mid
        return low






# @lc code=end
