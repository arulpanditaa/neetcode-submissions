class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [0] * n 
        dp[0] = 1

        for i in range(m):
            for j in range(n):
                if j > 0:
                    dp[j] = dp[j] + dp[j-1]
                
        return dp[n-1]
            


        
 
        