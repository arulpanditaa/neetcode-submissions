class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [nums[0]]

        for i in range(1, len(nums)):
            if tails[-1] < nums[i]:
                tails.append(nums[i])
                continue 
            left = 0 
            right = len(tails) - 1
            while right > left:
                mid = left + (right-left) // 2
                if tails[mid] < nums[i]:
                    left = mid+1
                else:
                    right = mid 
            tails[left] = nums[i]
        return len(tails)

            
                     


        




        