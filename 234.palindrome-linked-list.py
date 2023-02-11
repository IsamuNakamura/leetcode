#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals == vals[::-1]
        # count = 0
        # all_vals = []
        # while head:
        #     count += 1
        #     all_vals.append(head.val)
        #     head = head.next

        # way, back = [], []
        # half = (len(all_vals)-1)//2
        # print(half)
        # if count % 2 == 0:
        #     way = all_vals[:half+1]
        #     back = all_vals[half+1:]
        # else:
        #     way = all_vals[:half]
        #     back = all_vals[half+1:]

        # if len(way) != len(back):
        #     return False

        # while way:
        #     if way.pop() != back.pop(0):
        #         return False
        # return True



# @lc code=end
