class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        answer_area = 0 

        while left < right:
            current_area = (right - left) * min(heights[right], heights[left])
            answer_area = max(answer_area, current_area)
            if heights[left] > heights[right]:
                right -= 1
            else: 
                left += 1
        return answer_area
                
                

                


