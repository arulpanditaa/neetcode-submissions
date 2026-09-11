class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        def btrack(i, sol):
            if i == len(sol):
                res.append(sol[:])
                return None
            for j in range(i, len(sol)): 
                sol[i], sol[j] = sol[j], sol[i]
                btrack(i+1, sol)
                sol[i], sol[j] = sol[j], sol[i]
           
        btrack(0, nums)
        return res
            

            
        