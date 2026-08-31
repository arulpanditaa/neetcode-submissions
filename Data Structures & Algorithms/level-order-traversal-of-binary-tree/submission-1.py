# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        dq = deque()
        dq.append(root)

        while dq:
            curr_len = len(dq)
            level = []
            for i in range(curr_len):
                curr = dq.popleft()
                if curr:
                    level.append(curr.val)
                    if curr.left:
                        dq.append(curr.left)
                    if curr.right:
                        dq.append(curr.right)
            if level:
                res.append(level)
        return res 
            

