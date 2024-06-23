# https://leetcode.com/problems/add-two-numbers/
#
# Intuition:
# - This is my second pass at this problem
# - I need two pointers, one for the current node of each list()
# - I need to handle the case where one list is longer than the other
# - I will create the new LL as I traverse the others
# - Since every node only holds one digit, I only need to worry about an overflow of
#   1 each time
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        carry = 0
        while l1 or l2:
            new = carry
            if l1:
                new += l1.val
                l1 = l1.next
            if l2:
                new += l2.val
                l2 = l2.next
            carry = 1 if new > 9 else 0
            new -= 10 if new > 9 else 0
            curr.val = new
            if l1 or l2:
                curr.next = ListNode()
                curr = curr.next
            elif carry == 1:
                curr.next = ListNode(1)
        return head

