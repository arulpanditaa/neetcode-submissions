class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res, sol = [], []
        candidates.sort()

        def btrack(i, sums):
            if sums == target:
                res.append(sol[:])
                return None 
            if i >= len(candidates) or sums > target:
                return None 
            sol.append(candidates[i])
            btrack(i+1, sums + candidates[i])
            sol.pop()

            while (i+1) < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            btrack(i+1, sums)
        btrack(0, 0)
        return res

        