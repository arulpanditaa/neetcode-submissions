# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head 
        prevgrp = dummy

        while True:
            kth = prevgrp 
            count = 0
            while kth and count < k:
                kth = kth.next
                count += 1 
            if count < k or not kth:
                break 
            nextgrp = kth.next 

            prev = nextgrp
            curr = prevgrp.next
            for i in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt 
            
            tmp = prevgrp.next 
            prevgrp.next = kth 
            prevgrp = tmp

        return dummy.next  

        