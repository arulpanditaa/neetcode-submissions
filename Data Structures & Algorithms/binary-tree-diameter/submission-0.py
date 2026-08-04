# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        max_dia = 0 

        def getH(node):

            nonlocal max_dia

            if not node:
                return 0 

            left_h = getH(node.left)
            right_h = getH(node.right)

            max_dia = max(max_dia, left_h + right_h)
            return ( 1 + max(left_h, right_h))

        getH(root)

        return max_dia

        
        