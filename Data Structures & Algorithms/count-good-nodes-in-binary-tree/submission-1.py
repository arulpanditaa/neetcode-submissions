# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        answer = 0

        def dfs(node, highest):
            if not node:
                return None
            nonlocal answer
            if node.val >= highest:
                answer += 1
                highest = node.val
            dfs(node.left, highest)
            dfs(node.right, highest)

        dfs(root, root.val)

        return answer
        