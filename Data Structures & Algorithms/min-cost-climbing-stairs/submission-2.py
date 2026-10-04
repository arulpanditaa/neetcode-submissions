class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        prev_prev, prev = cost[0], cost[1]

        for i in range(2, len(cost)):
            curr = cost[i] + min(prev_prev, prev)
            prev, prev_prev = curr, prev 
        
        return min(prev, prev_prev)



        



        

        
        