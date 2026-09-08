class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = [[]]

        for num in nums:
            sols = []
            for sol in res:
                sols.append(sol + [num])
            res += sols
        return res
        