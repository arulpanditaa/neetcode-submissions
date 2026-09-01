# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, highest):
            if not node:
                return 0
            ans = 0
            if node.val >= highest:
                ans = 1
                highest = node.val

            ans += dfs(node.left, highest)
            ans += dfs(node.right, highest)
            return ans


        return dfs(root, root.val)

        
        