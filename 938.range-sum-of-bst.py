#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        self.ans = 0
        def dfs(root: Optional[TreeNode]):
            if root == None:
                return
            if low <= root.val <= high:
                self.ans += root.val

            if root.val > low:
                dfs(root.left)
            if root.val < high:
               dfs(root.right)

        dfs(root)
        return self.ans

# @lc code=end
