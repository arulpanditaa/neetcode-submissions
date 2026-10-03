class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1

        prev, curr = 1, 2
        for j in range(3, n+1):
            curr, prev = curr+prev, curr
        return curr
             

        

        
        