# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        prev = dummy
        curr1 = l1 
        curr2 = l2
        carry = 0

        while curr1 or curr2 or carry:
            if curr1:
                val1 = curr1.val 
                curr1 = curr1.next
            else:
                val1 = 0
            if curr2:
                val2 = curr2.val 
                curr2 = curr2.next
            else:
                val2 = 0 
            total = val1 + val2 + carry 
            number = total % 10 
            carry = total // 10
            prev.next = ListNode(number)
            prev = prev.next 
             
        return dummy.next     
        