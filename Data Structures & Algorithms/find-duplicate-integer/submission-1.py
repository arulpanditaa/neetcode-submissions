class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        curr1 = 0 
        fast = 0 

        while nums[curr1] and nums[nums[fast]]:
            curr1 = nums[curr1]
            fast = nums[nums[fast]]
            if fast == curr1:
                break 
        curr2 = 0 
        while nums[curr2] and nums[curr1]:
            curr2 = nums[curr2]
            curr1 = nums[curr1]
            if curr1 == curr2:
                return curr1
                

        