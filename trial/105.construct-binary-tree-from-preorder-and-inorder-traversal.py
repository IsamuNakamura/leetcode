#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        preorderNode = preorder[0]
        node = TreeNode(preorderNode)
        inorderIdx = inorder.index(node.val)

        node.left = self.buildTree(preorder[1:], inorder[:inorderIdx])
        node.right = self.buildTree(preorder[inorderIdx+1:], inorder[inorderIdx+1:])

        return node


# @lc code=end
