class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Myset = set()

        for i in nums:
            if i in Myset:
                return True
            else: Myset.add(i)
        
        return False 

        
        