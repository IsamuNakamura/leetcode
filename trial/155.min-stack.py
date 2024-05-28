#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.list = []
        self.min_list = []

    def push(self, val: int) -> None:
        self.list.append(val)
        if len(self.min_list) <= 0:
            self.min_list.append(val)
        elif val <= self.min_list[-1]: # 最小で同じ値は追加しておく(①のため)
            self.min_list.append(val)

    def pop(self) -> None:
        last = self.list.pop()
        if len(self.min_list) > 0 and self.min_list[-1] == last: # ①
            self.min_list.pop()

    def top(self) -> int:
        if len(self.list) < 0:
            return 0
        else:
            return self.list[-1]

    def getMin(self) -> int:
        if len(self.min_list) <= 0:
            return 0
        else:
            return self.min_list[-1]




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end
