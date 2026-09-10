class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res, sol = [], []
        candidates.sort()
        
        def btrack(i, sums):
            if sums == target:
                res.append(sol[:])
                return None
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue 
                if sums + candidates[j] > target:
                    return None
                sol.append(candidates[j])
                btrack(j + 1, sums + candidates[j])
                sol.pop()
                

        btrack(0, 0)
        return res
