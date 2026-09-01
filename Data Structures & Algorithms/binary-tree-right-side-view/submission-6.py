# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        dq = deque()
        dq.append(root)

        while dq:
            level_len = len(dq)
            for i in range(level_len):
                curr = dq.popleft()
                if curr:
                    if curr.left:
                        dq.append(curr.left)
                    if curr.right:
                        dq.append(curr.right)
            if curr:
                res.append(curr.val)
        
        return res
            
            
            






        
        