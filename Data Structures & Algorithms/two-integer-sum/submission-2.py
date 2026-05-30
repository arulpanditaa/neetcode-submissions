class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, num in enumerate(nums):
            answer = target - num 
            if answer in dict:
                return [dict[answer], i]
            dict[num] = i 

        