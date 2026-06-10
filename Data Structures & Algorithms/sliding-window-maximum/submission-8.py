class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        left = 0
        lists = []
        answer = []

        for right in range(len(nums)):
            while lists and nums[right] >= nums[lists[-1]]:
                lists.pop()
            lists.append(right)

            if lists[0] < left:
                lists.pop(0)

            if (right-left+1) == k:
                answer.append(nums[lists[0]])
                left += 1
        return answer 
        
        