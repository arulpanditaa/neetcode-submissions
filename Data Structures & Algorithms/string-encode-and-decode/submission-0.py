class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_words = []

        for word in strs:

            encoded_words.append(str(len(word)))
            encoded_words.append("#")
            encoded_words.append(word)            
        
        encoded_string = "".join(encoded_words)
        return encoded_string

    def decode(self, s: str) -> List[str]:

        decoded_string = []

        i = 0

        while i < len(s):

            j = i
            while s[j] != "#":
                j += 1

            if s[j] == "#":
                length = int(s[i:j])
                word = s[j+1:j+1+length]
                decoded_string.append(word)
            
            i = j + 1 + length 

        return decoded_string