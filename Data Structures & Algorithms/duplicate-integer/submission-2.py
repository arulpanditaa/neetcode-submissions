class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        MySet = set()

        for i in nums:

            if i in MySet:
                return True
            else: 
                MySet.add(i)
        return False

        
        
        