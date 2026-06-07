class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = prices[0]
        real_profit = 0

        for i, sell in enumerate(prices):
            
            while sell < buy:
                buy = sell
            
            profit = sell - buy

            real_profit = max(profit, real_profit)

        return real_profit
        
        
    
        
        