class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        count = defaultdict(int)
        res, sol, unique = [], [], []
        for num in candidates:
            if count[num] == 0:
                unique.append(num)
            count[num] += 1 

        def btrack(i, sums):
            if sums == target:
                res.append(sol[:])
                return None
            for j in range(i, len(unique)):
                if sums + unique[j] > target:
                    continue 
                if count[unique[j]] == 0:
                    continue 
                sol.append(unique[j])
                count[unique[j]] -= 1 
                btrack(j, sums + unique[j])
                count[unique[j]] += 1
                sol.pop()
        btrack(0,0) 
        return res

                

            




        
        