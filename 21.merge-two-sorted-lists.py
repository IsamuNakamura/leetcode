#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0)
        runner = ans

        while list1 and list2:
            if list1.val > list2.val:
                runner.next = list2
                list2 = list2.next
            else:
                runner.next = list1
                list1 = list1.next
            runner = runner.next
        runner.next = list1 or list2 # important
        return ans.next

# @lc code=end
