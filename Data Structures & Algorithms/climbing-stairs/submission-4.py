class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = defaultdict(int)
        cache[n] = 1
        cache[n+1] = 0
        def dfs(i):
            if i >= n:
                return i == n
            if cache[i]:
                return cache[i]
            cache[i] = dfs(i+1) + dfs(i+2) 
            return cache[i]
        return dfs(0)
             

        

        
        