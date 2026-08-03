# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0 

        dq = deque([(root, 1)])
        max_depth = 0 

        while dq:
            curr, depth = dq.popleft()
            max_depth = max(depth, max_depth)

            if curr.left:
                dq.append((curr.left, depth+1))
            if curr.right:
                dq.append((curr.right, depth+1))
        return max_depth

        