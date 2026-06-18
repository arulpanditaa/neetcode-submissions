# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def merge2lists(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy 
        while l1 and l2:
            if l1.val > l2.val:
                curr.next = l2
                l2 = l2.next 
            else:
                curr.next = l1
                l1 = l1.next 
            curr = curr.next 
        if l1:
            curr.next = l1
        else:
            curr.next = l2
        return dummy.next 
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None 
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                if i+1 < len(lists):
                    l2 = lists[i+1]
                else:
                    l2 = None 
                winner = self.merge2lists(l1, l2)
                merged_lists.append(winner)
            lists = merged_lists 
        return lists[0]


        
        