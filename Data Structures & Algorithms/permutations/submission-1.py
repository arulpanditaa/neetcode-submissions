class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        
        def btrack(sol, pick):
            if len(sol) == len(nums):
                res.append(sol[:])
                return None
            for j in range(len(nums)):
                if not pick[j]:
                    pick[j] = True
                    sol.append(nums[j])
                    btrack(sol, pick)
                    pick[j] = False
                    sol.pop()
                
        btrack([], len(nums)* [False])
        return res 
            

        