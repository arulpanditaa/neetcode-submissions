class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [float("inf")] * (amount+1)
        dp[0] = 0 

        for i in range(1, len(dp)):
            for j in range(len(coins)):
                ans = i - coins[j]
                if ans < 0:
                    continue  
                dp[i] = min(dp[ans] + 1, dp[i])

        if dp[amount] == float("inf"):
            return -1
        else:
            return dp[amount]
                



        