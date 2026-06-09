class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        left = 0
        have = 0
        score1 = defaultdict(int)
        score2 = defaultdict(int)
        for char in t:
            score2[char] += 1
        need = len(score2)
        length = 10000
        range_len = [len(s), len(t)]
        for right in range(len(s)):
            score1[s[right]] += 1 
            if s[right] in score2 and score1[s[right]] == score2[s[right]]:
                have += 1
            while have == need:
                if (right - left + 1) < length:
                    length = right - left + 1 
                    range_len = [left, right]
                score1[s[left]] -= 1 
                if s[left] in score2 and score1[s[left]] < score2[s[left]]:                 
                    have -= 1
                left += 1
        if length < 1000:
            return s[range_len[0]:range_len[1] + 1]
        else:
            return ""
             
        

                

             


