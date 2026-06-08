class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        left = 0
        score1 = defaultdict(int)
        score2 = defaultdict(int)
        for char in s1:
            score1[char] += 1

        for right in range(len(s2)):
            score2[s2[right]] += 1 
            if (right - left + 1) == len(s1):
                if score1 == score2:
                    return True
                else:
                    score2[s2[left]] -= 1
                    if score2[s2[left]] == 0:
                        del score2[s2[left]]
                    left += 1

        return False


        