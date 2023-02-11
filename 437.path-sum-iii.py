#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        def dfs(node, targetSum):
            if not node:
                return 0
            cnt = 0
            if node.val == targetSum:
                cnt += 1
            cnt += dfs(node.left, targetSum - node.val)
            cnt += dfs(node.right, targetSum - node.val)
            return cnt

        return dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)


# @lc code=end
