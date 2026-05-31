class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_map = defaultdict(int)

        for num in nums:
            freq_map[num] += 1
        
        answer = defaultdict(list)
        for num, freq in freq_map.items():
            answer[freq].append(num)

        result =[]
        for i in sorted(answer.keys(), reverse = True):

            for num in answer[i]:
                result.append(num)
                
                if len(result) == k:
                    return result