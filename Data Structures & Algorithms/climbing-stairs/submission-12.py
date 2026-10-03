class Solution:
    def climbStairs(self, n: int) -> int:
        
        prev, curr = 1, 2 

        if n == 1:
            return 1
        if n == 2:
            return 2 
        
        def dp(): 
            nonlocal curr
            nonlocal prev
            for j in range(3, n+1):
                curr, prev = curr+prev, curr
            return curr
        
        return dp()
             

        

        
        