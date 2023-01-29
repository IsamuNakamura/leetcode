#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashMap = {}
        while head != None:
            if head.val <= - 10 ** 5 or 10 ** 5 <= head.val:
                return False

            if head in hashMap:
                return True
            else:
                hashMap[head] = head
            head = head.next
        return False

# @lc code=end

# head: Optional[ListNode] = [1,2]\npos = 0
