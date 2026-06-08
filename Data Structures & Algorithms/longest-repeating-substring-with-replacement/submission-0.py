class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        answer = 0
        scoreboard = defaultdict(int)
        
        for right in range(len(s)):
            scoreboard[s[right]] += 1 
            length = right - left + 1
            max_freq = max(scoreboard.values())
            limit = length - max_freq
            while limit > k:
                scoreboard[s[left]] -= 1 
                left += 1
                length = right - left + 1 
                max_freq = max(scoreboard.values())
                limit = length - max_freq
            answer = max(length, answer)
        return answer 

            
        