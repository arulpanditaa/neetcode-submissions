class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = [[]]

        for num in nums:
            sols = []
            for sol in res:
                new_sol = sol + [num]
                sols.append(new_sol)
            res += sols
        return res
        