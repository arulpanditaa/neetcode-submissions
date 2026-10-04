class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        prev_p, prev = 0, 0
        curr = 0

        for i in range(2, len(cost)+1):
            curr = min(prev_p + cost[i-2], prev + cost[i-1])
            prev, prev_p = curr, prev 
        
        return curr



        



        

        
        