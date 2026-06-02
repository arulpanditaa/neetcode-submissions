class Solution:

    def encode(self, strs: List[str]) -> str:

        words_combined = []
        for word in strs:
            words_combined.append(str(len(word)))
            words_combined.append("#")
            words_combined.append(word)
        encoded_string = "".join(words_combined)   

        return encoded_string     

    def decode(self, s: str) -> List[str]:

        i = 0
        decoded_strs = [] 
        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1 
            if s[j] == "#":
                length = int(s[i:j])
                decoded_strs.append(s[j+1:j+1+length])
            i = j + 1 + length
        
        return decoded_strs
