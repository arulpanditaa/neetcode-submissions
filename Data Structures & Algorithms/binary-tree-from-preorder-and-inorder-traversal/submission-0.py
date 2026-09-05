# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        index = {}
        for i, val in enumerate(inorder):
            index[val] = i
        
        pre_idx = 0        
        def dfs(left, right):
            if left > right:
                return None 
            nonlocal pre_idx
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)

            pre_idx += 1 
            mid = index[root_val]

            root.left = dfs(left , mid - 1)
            root.right = dfs(mid + 1, right) 
            return root 
        return dfs(0, len(index) - 1)





            

        
        
        