class Solution:
    def rob(self, nums: List[int]) -> int:

        prev, curr_max = 0, 0

        for i in range(len(nums)):
            new_max = max(prev + nums[i], curr_max)
            prev, curr_max = curr_max, new_max 
            
        return curr_max


