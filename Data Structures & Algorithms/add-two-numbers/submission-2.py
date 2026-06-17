# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        num1 =l1
        num2 =l2
        carry = 0
        dummy = ListNode(0)
        curr = dummy

        while num1 or num2 or carry:
            if num1:
                val1 = num1.val
                num1 = num1.next 
            else:
                val1 = 0
            if num2:
                val2 = num2.val
                num2 = num2.next
            else:
                val2 = 0 
            total = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10
            new_node = ListNode(total)
            curr.next = new_node
            curr = curr.next 
        return dummy.next 

        