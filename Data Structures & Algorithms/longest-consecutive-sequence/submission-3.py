class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        ovr_streak = 0

        for num in num_set:

            if  num-1 not in num_set:

                streak = 1

                while num + streak in num_set:
                    streak += 1
                if streak > ovr_streak:     
                    ovr_streak = streak 

        return ovr_streak

        
        