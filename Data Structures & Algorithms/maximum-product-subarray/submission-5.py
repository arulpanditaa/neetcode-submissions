class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        ans = nums[0]
        p_max, p_min = nums[0], nums[0]
        for i in range(1, len(nums)):
            curr_min = min(p_min*nums[i], p_max*nums[i], nums[i])
            curr_max = max(p_max*nums[i], p_min*nums[i], nums[i])
            p_max, p_min = curr_max, curr_min
            ans = max(curr_max, ans)
        return ans 


        