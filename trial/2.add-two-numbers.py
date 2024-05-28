#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = ListNode(0)
        # update pointer at every iteration
        # same reference
        pointer = result

        while(l1 != None or l2 != None or carry != 0):
            num1 = l1.val if l1 is not None else 0
            num2 = l2.val if l2 is not None else 0

            sum = num1 + num2 + carry
            num = sum % 10
            carry = sum // 10

            print(num)
            print(carry)

            pointer.next = ListNode(num)
            pointer = pointer.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next

# @lc code=end
