# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q:   TreeNode) -> TreeNode:
    
        ans = root
        while ans:
            if ans.val > p.val and ans.val > q.val:
                ans = ans.left
            elif ans.val < p.val and ans.val < q.val:
                ans = ans.right
            else:
                break 
        def exists(node, target):
            curr = root
            while curr:
                if target.val > curr.val:
                    curr = curr.right
                elif target.val < curr.val:
                    curr = curr.left
                else:
                    return True
            return False 
        if exists(root, p) and exists(root, q):
            return ans
            
        

