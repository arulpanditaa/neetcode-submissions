class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1 


        sort = []
        for i in range(len(nums) + 1):
            sort.append([])
    

        for num, freq in freq_map.items():
            sort[freq].append(num)

        answer = []
        for i in range(len(sort) - 1, 0, -1):
            for num in sort[i]:
                answer.append(num)
            
            if (len(answer) == k):
                return answer

        





        
        