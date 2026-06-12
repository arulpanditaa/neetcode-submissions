# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head 
        prev = dummy 
        curr = head 
        nxt = curr.next
        number = 0
        police = head
        front = 0

        while police:
            number += 1 
            police = police.next 

        while curr and curr.next:
            if front == number - n:
                prev.next = nxt 
                curr = nxt
                return dummy.next 
            else:
                curr = curr.next 
                nxt = curr.next 
                prev = prev.next
            front += 1 

        if front == number -n:
            prev.next = None  
            return dummy.next
        
        return dummy.next
        