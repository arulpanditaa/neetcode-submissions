# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        
        last = None
        heights = {}
        stack = []
        node = root 

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if node.right and last != node.right:
                    node = node.right 
                else:
                    stack.pop()
                    left = heights.get(node.left, 0)
                    right = heights.get(node.right, 0)

                    heights[node] = max(left,right) + 1 

                    if abs(left - right) > 1:
                        return False

                    last = node
                    node = None    
        return True                  



        


        