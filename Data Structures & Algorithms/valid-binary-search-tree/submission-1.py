# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        dq = deque()
        dq.append([root, float("-inf"), float("inf")])

        while dq:
            curr, left, right = dq.popleft()
            if curr.val <= left or curr.val >= right:
                return False
            if curr.left:
                dq.append([curr.left, left, curr.val])
            if curr.right:
                dq.append([curr.right, curr.val, right])
            
        return True 