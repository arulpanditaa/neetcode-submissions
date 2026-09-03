# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        arr = []
        ans = 0
        count = 0 

        def dfs(node):
            if not node:
                return None 
            nonlocal ans
            nonlocal count 
            dfs(node.left)
            arr.append(node.val)
            count += 1
            if count == k:
                ans = node.val
            dfs(node.right)
         
        dfs(root)

        return ans
        

        