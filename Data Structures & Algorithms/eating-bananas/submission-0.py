class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        slowest = 1
        answer = max(piles)

        while slowest < answer:
            mid = slowest + (answer - slowest) // 2 
            total_hours = 0
            for pile in piles:
                hours_spent = (pile + mid - 1) // mid
                total_hours += hours_spent 
            if total_hours > h:
                slowest = mid + 1 
            else: 
                answer = mid 
        return answer 
            
                  
        