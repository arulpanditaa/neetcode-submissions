class Solution:
 def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

    result = defaultdict(list)

    for word in strs:

        freq = {}

        for letter in word:

            freq[letter] = freq.get(letter, 0) + 1 

        key = tuple(sorted(freq.items()))

        result[key].append(word)

    return list(result.values())