class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) < 2:
            return nums[0]

        prev, maxx = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            new_max = max(prev + nums[i], maxx)
            prev, maxx = maxx, new_max 

        return maxx