class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n_hold, p_n_hold, p2_n_hold, hold = 0, 0, 0, float("-inf")
        for i in range(1, len(prices)+1):
            p2_n_hold = p_n_hold
            p_n_hold = n_hold
            n_hold = max(n_hold, hold + prices[i-1])
            hold = max(p2_n_hold - prices[i-1], hold)
        
        return n_hold




