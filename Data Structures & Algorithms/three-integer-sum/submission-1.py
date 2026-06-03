class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        answer = []
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            fixed = num
            left = i + 1 
            right = (len(nums) - 1)
            while left < right:
                sums = fixed + nums[left] + nums[right]
                if sums == 0:
                    answer.append([fixed, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left< right and nums[left] == nums[left-1]:
                        left += 1
                elif sums > 0:
                    right -= 1
                elif sums < 0:
                    left += 1
        return answer



        