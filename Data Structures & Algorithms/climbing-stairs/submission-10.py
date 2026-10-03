class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = defaultdict(int)
        cache[1], cache[2] = 1, 2 
        
        def dp(): 
            for j in range(3, n+1):
                cache[j] = cache[j-1] + cache[j-2]
            return cache[n]
        
        return dp()
             

        

        
        