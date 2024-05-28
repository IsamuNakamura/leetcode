#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        result = ListNode(0)
        pointer = result
        pointer.next = ListNode(head.val)
        pointer = pointer.next
        head = head.next
        while head != None:
            if pointer.val != head.val:
                pointer.next = ListNode(head.val)
                pointer = pointer.next
            head = head.next
        return result.next

        # runner = head
        # while runner != None:
        #     while runner.next and runner.val == runner.next.val:
        #             runner.next = runner.next.next
        #     runner = runner.next
        # return head

# @lc code=end
