#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def dfs(left, right: TreeNode)-> bool:
            if left and right:
                return left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)
            else:
                return left == right

        return dfs(root.left, root.right)

# @lc code=end
