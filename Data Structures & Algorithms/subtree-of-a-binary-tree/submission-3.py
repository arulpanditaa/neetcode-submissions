# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot:
            return True 
        if not root:
            return False 
        dq = deque()
        dq.append(root)

        while dq:
            node = dq.popleft()
            if not node:
                continue
            if self.SameTree(node, subRoot):
                return True
            dq.append(node.left)
            dq.append(node.right)
        return False
    def SameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        stack = [(p,q)]

        while stack:
            node1 , node2 = stack.pop()

            if not node1 and not node2:
                continue 
            if not node1 or not node2 or node1.val != node2.val:
                return False
            stack.append((node1.right, node2.right))
            stack.append((node1.left, node2.left))
        return True 
            

    


            
                





        