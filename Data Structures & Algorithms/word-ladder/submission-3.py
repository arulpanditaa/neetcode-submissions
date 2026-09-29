class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        patterns, dq = defaultdict(list), deque()
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                patterns[pattern].append(word)
        dq.append([beginWord, 1])
        seen = {beginWord}
        while dq:
            word, depth = dq.popleft()
            for i in range(len(word)):
                pat = word[:i] + "*" + word[i+1:]
                for nxt_word in patterns[pat]:
                    if nxt_word == endWord:
                        return (depth + 1)
                    if nxt_word not in seen:
                        dq.append([nxt_word, depth+1])
                        seen.add(nxt_word)
                #patterns[pat] = [] # A trick but seen still takes care of this even without this line of code.
        return 0
                    
                    

                    

        
        
         

        