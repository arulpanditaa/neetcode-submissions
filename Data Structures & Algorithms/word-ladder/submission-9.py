class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord or endWord not in wordList:
            return 0 
        patterns, dq1, dq2 = defaultdict(list), deque(), deque()
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                patterns[pattern].append(word)
        dq1.append(beginWord)
        dq2.append(endWord)
        seen1, seen2 = {beginWord: 1}, {endWord: 1}
        while dq1 and dq2:
            if len(dq1) > len(dq2):
                dq1, dq2 = dq2, dq1
                seen1, seen2 = seen2, seen1
            for i in range(len(dq1)):
                word = dq1.popleft()
                steps = seen1[word]
                for i in range(len(word)):
                    pat = word[:i] + "*" + word[i+1:]
                    for nxt_word in patterns[pat]:
                        if nxt_word in seen2:
                            return (steps + seen2[nxt_word])
                        if nxt_word not in seen1:
                            dq1.append(nxt_word)
                            seen1[nxt_word] = steps + 1
        return 0
                    
                    

                    

        
        
         

        