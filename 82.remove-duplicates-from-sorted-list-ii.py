#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        results = ListNode(0)
        results.next = head
        prev, cur = results, head
        print(prev.val)
        print(prev.next.val)
        while cur:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            if prev.next == cur:
                print(cur.val)

                prev = prev.next
            else:
                prev.next = cur.next
            cur = cur.next
        return results.next

# @lc code=end
