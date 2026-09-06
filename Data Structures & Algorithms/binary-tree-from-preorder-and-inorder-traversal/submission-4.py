# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        head = TreeNode(None)
        curr = head
        pre_ord, in_ord, n = 0, 0, len(preorder)

        while pre_ord < n and in_ord < n:
            curr.right = TreeNode(preorder[pre_ord], right = curr.right)
            curr = curr.right
            pre_ord += 1

            while pre_ord < n and curr.val != inorder[in_ord]:
                curr.left = TreeNode(preorder[pre_ord], right = curr)
                curr = curr.left
                pre_ord += 1 
            in_ord += 1 

            while curr.right and in_ord < n and curr.right.val == inorder[in_ord]:
                prev = curr.right
                curr.right = None 
                curr = prev
                in_ord += 1 
                 

        return head.right




