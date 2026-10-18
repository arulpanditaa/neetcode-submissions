class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        sums = 0 
        for num in nums:
            sums += num
        if abs(target) > sums or (sums+target) % 2 != 0:
            return 0 
        sub_target = (target + sums) // 2 

# P - N = target, P + N = sums, 2P = target + sums.     P = (target+sums) // 2, find P, subsets sum to P/N = no of ways to reach the target (P-N), that is the ans.   
        dp = [0] * (sub_target+1)
        dp[0] = 1

        for num in nums:
            for i in range(sub_target, num - 1, -1):
                dp[i] += dp[i - num]
        
        return dp[sub_target]

        
        