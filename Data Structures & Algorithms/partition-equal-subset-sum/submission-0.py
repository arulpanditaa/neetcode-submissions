class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2 

        dp = [False] * (target+1)
        dp[0] = True

        for i in range(len(nums)):
            for sums in range(target, nums[i] - 1, -1):
                dp[sums] = dp[sums] or dp[sums - nums[i]]
        
        return dp[target]



