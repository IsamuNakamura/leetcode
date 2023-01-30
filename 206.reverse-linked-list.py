#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        stack = []
        current_node = head
        while current_node != None:
            stack.append(current_node.val)
            current_node = current_node.next

        reversed = head
        while reversed != None:
            reversed.val = stack.pop()
            reversed = reversed.next
        return head

# @lc code=end

# if __name__ == "__main__":
#     s = Solution()
#     l = [1,2,3,4,5]
#     ln = []

#     for i, v in enumerate(l):
#         if i < len(l)-2:
#             n = ListNode(v, l[i+1])
#         else:
#             n = ListNode(v)

#     print(l)
