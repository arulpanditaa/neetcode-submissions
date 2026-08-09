# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        dq1 = deque()
        dq2 = deque()

        dq1.append(p)
        dq2.append(q)

        while dq1 and dq2:
           for i in range(len(dq1)): 

            node1 = dq1.popleft()
            node2 = dq2.popleft()

            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            dq1.append(node1.left)
            dq1.append(node1.right)
            dq2.append(node2.left)
            dq2.append(node2.right)

        return True


        
        