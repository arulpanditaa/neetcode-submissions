class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        res = []

        def btrack(i, sums, sol):
            if sums == target:
                res.append(sol[:])
                return None
            
            for j in range(i, len(nums)):
                if sums + nums[j] > target:
                    return None 
                sol.append(nums[j])
                btrack(j, sums + nums[j], sol)
                sol.pop()
        btrack(0, 0, [])
        return res 
        