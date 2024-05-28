#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashMap = {}
        while head != None:
            if head.val <= - 10 ** 5 or 10 ** 5 <= head.val:
                return None

            if head in hashMap:
                return head
            hashMap[head] = head
            head = head.next

        return head

# @lc code=end
