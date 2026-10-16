class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(1, len(dp)):
                if i - coin >= 0:
                    dp[i] += dp[i - coin]
        
        return dp[amount]

# Put the coin loop outside and amount loop inside so combinations are built in a fixed coin order; so when dp[3] first uses dp[2] during the coin = 1 pass, dp[2] it's still 1 (only 1+1), and it becomes 2 only later when coin 2 is processed, preventing 1+2 and 2+1 from being double-counted.

# dp[i] = number of combinations to make amount i 