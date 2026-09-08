class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        def btrack(i, sol):
            if i >= len(nums):
                res.append(sol)
                return None
            btrack(i+1, sol)

            btrack(i+1, sol + [nums[i]])
        
        btrack(0, [])
        return res

        
        