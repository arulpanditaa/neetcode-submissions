"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None 
        curr = head
        while curr:
            copy_node = Node(curr.val)
            copy_node.next = curr.next 
            curr.next = copy_node
            curr = copy_node.next 
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next 
            curr = curr.next.next
        curr = head 
        copy_node = head.next
        curr_copy = copy_node  
        while curr:
            curr.next = curr.next.next
            if curr_copy.next:
                curr_copy.next = curr_copy.next.next
            curr = curr.next 
            curr_copy = curr_copy.next 
        return copy_node 


        