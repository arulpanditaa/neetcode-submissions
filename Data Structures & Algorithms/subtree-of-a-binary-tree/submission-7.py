# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root == None:
            return "$#"
        
        return (str(root.val) + self.serialize(root.left) + self.serialize(root.right))
    
    def z_func(self, s: str) -> list: 
        z = [0] * len(s)
        l, r, n = 0, 0, len(s)
        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
    # The 2nd condition checks how many elements of the str and sub-str match. 
                z[i] += 1
            if i - 1 + z[i] > r:
#(i - 1) is the element just before the left boundary and adding z[i] to it will give you the right boundary. 
                l, r = i , i - 1 + z[i]
        return z 

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        s_root = self.serialize(root)
        s_subRoot = self.serialize(subRoot)
        combined = s_subRoot + "|" + s_root

        z_values = self.z_func(combined)
        sub_len = len(s_subRoot)

        for i in range(sub_len + 1, len(combined)):
            if z_values[i] == sub_len:
                return True 
        return False 
        