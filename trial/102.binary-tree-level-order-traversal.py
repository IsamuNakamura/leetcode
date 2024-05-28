#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
from collections import defaultdict
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = defaultdict(list)
        level = 0
        def dfs(root, level):
            if root == None:
                return
            ans[level].append(root.val)
            dfs(root.left, level+1)
            dfs(root.right, level+1)
        dfs(root, level)
        return ans.values()



# @lc code=end
