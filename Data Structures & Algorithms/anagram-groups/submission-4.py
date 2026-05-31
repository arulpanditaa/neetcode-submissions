class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        master_dict = defaultdict(list)

        for words in strs:

            count = [0] *26

            for letter in words:
                count[ord(letter) - ord('a')] += 1
            dna = tuple(count)  
            
            master_dict[dna].append(words)      
        return list(master_dict.values())


