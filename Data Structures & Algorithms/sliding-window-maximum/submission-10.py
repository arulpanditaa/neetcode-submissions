class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        left = 0
        lists = deque()
        answer = []

        for right in range(len(nums)):
            if lists and lists[0] < left:
                lists.popleft()

            while lists and nums[right] >= nums[lists[-1]]:
                lists.pop()
            lists.append(right)

            if (right-left+1) == k:
                answer.append(nums[lists[0]])
                left += 1
        return answer 
        
        