class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic = {}

        for i, n in enumerate(nums):

            answer = target - n 

            if answer in dic:
                return [dic[answer], i]
            else:
               dic[n] = i 
        
        return []






        
        
        
        
