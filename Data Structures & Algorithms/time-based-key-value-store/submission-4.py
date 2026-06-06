class TimeMap:
    def __init__(self):
        self.data = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key].append((value, timestamp))
        else:
            self.data[key] = [(value, timestamp)]        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        timeline = self.data[key]
        left = 0 
        right = len(timeline) - 1
        answer = ""

        while right >= left:
            mid = left + (right - left) // 2
            if timeline[mid][1] <= timestamp:
                answer = timeline[mid][0]
                left = mid + 1 
            else:
                right = mid - 1 
        return answer 



        
