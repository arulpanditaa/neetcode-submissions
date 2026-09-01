# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        answer = 0
        dq = deque()
        dq.append([root, root.val])

        while dq:
            curr, highest = dq.popleft()

            if curr.val >= highest:
                answer += 1 
                highest = curr.val
            if curr.left:
                dq.append([curr.left, highest])
            if curr.right:
                dq.append([curr.right, highest])
        return answer

        