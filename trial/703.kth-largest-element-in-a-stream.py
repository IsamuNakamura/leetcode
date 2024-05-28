#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#
import heapq
# @lc code=start
class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        if k < 1 or 10000 < k:
            exit(-1)
        if 10000 < len(nums):
            exit(-1)

        for n in nums:
            if n < -10000 or 10000 < n:
                exit(-1)

        self.k_th = k
        self.list = []
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        if val < -10000 or 10000 < val:
            exit(-1)
        # 後ろから3番目に小さいデータを先頭に持っていく
        heapq.heappush(self.list, val)
        if len(self.list) > self.k_th:
            heapq.heappop(self.list)
        return self.list[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

kthLargest = KthLargest(3, [4, 5, 8, 2]);
print(kthLargest.add(3))
print(kthLargest.add(5))
print(kthLargest.add(10))
print(kthLargest.add(9))
print(kthLargest.add(4))
