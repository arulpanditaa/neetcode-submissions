# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head 
        fast = head.next  
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        second = slow.next 
        slow.next = None 
        prev = None 
        while second:
            nxt = second.next 
            second.next = prev 
            prev = second
            second = nxt
        second = prev 
        first = head 
        while second:
            nxt1 = first.next
            first.next = second
            nxt2 = second.next
            second.next = nxt1
            first = nxt1
            second = nxt2  

        