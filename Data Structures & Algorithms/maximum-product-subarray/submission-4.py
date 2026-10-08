class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        ans = max(float("-inf"), nums[0])
        prev_max, prev_min = nums[0], nums[0]
        for i in range(1, len(nums)):
            curr_min = min(prev_min*nums[i], prev_max*nums[i], nums[i])
            curr_max = max(prev_max*nums[i], prev_min*nums[i], nums[i])
            prev_max, prev_min = curr_max, curr_min
            ans = max(curr_max, ans)
        
        return ans 


        