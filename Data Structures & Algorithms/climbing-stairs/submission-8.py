class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = defaultdict(int)
        cache[1], cache[2] = 1, 2 
    
        def dfs(i):
            if cache[i]:
                return cache[i]
            cache[i] = dfs(i-1) + dfs(i-2) 
            return cache[i]
        return dfs(n)
# False + True = 1, True + True = 2
             

        

        
        