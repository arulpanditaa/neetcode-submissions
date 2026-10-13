class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = []
        for i in range(len(prices)+1):
            row = []
            for j in range(2):
                row.append(0)
            dp.append(row)
        dp[0][1] = float("-inf")
        
        for i in range(1, len(prices)+1):
        
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i-1])
# prices[i-1] = price on the i'th day. dp[i-1][0/1] = best profit after (i-1) days, if its 0 in the 2nd bracket then its not holding, if it's 1 then holding.
            dp[i][1] = max(dp[i-2][0] - prices[i-1], dp[i-1][1])
        
        return dp[len(prices)][0]




