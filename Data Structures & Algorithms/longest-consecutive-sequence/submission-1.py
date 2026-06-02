class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seq = set(nums)
        ovr_streak = 0

        for num in seq:

            if  num-1 not in seq:

                current_num = num
                streak = 1

                while current_num+1 in nums:
                    current_num += 1
                    streak += 1
                if streak > ovr_streak:     
                    ovr_streak = streak 

        return ovr_streak

        
        