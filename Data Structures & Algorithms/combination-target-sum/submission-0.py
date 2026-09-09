class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res, sol = [], []
        def btrack(i, sums):
    
            if sums == target:
                res.append(sol[:])
                return None 
            if i >= len(nums) or sums > target:
                return None         
            sol.append(nums[i])
            btrack(i, sums + nums[i])
            sol.pop()
            btrack(i+1, sums)
        btrack(0, 0)

        return res


