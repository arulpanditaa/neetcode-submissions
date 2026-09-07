# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best_thr_node = float('-inf') 
        def dfs(node):
            nonlocal best_thr_node
            if node == None:
                return 0 
            left = dfs(node.left)
            right = dfs(node.right)

            best_downward = node.val + max(0, left, right)

            curr_thr_node = node.val + max(0, left) + max(0, right)
            best_thr_node = max(curr_thr_node, best_thr_node)

            return best_downward
        dfs(root)
        return best_thr_node




        