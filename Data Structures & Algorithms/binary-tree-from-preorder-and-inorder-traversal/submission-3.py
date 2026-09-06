# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        pre_ord = 0
        in_ord = 0
        def dfs(stop):
            nonlocal in_ord, pre_ord
            if pre_ord >= len(preorder):
                return None 
            if inorder[in_ord] == stop:
                in_ord += 1 
                return None
            root_val = preorder[pre_ord]
            root = TreeNode(root_val)
            pre_ord += 1 

            root.left = dfs(root.val)
            root.right = dfs(stop)
            return root 
        return dfs(float('inf'))