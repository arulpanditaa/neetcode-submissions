class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        
        def dp(lower, upper):
            prev, curr_max = 0, 0 
            for i in range(lower, upper):
                new_max = max(prev + nums[i], curr_max)
                curr_max, prev = new_max, curr_max
            return curr_max
        
        return max(dp(0, len(nums)-1), dp(1, len(nums)))



        