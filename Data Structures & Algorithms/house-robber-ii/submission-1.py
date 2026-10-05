class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        prev1, curr_max1 = 0, 0 
        for i in range(len(nums) - 1):
            new_max1 = max(prev1 + nums[i], curr_max1)
            curr_max1, prev1 = new_max1, curr_max1

        prev2, curr_max2 = 0, 0
        for j in range(1, len(nums)):
            new_max2 = max(prev2 + nums[j], curr_max2)
            curr_max2, prev2 = new_max2, curr_max2
        
        return max(curr_max1, curr_max2)



        