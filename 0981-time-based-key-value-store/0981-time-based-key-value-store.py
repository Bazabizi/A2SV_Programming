class TimeMap:
    def __init__(self):
        self.d = defaultdict(list)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([timestamp, value])
    
    def get(self, key: str, timestamp: int) -> str:
        if key in self.d:
            arr = self.d[key]
            if timestamp >= arr[-1][0]:
                return arr[-1][1]
            if timestamp < arr[0][0]:
                return ""
            l, r = 0, len(arr) - 1
            while l < r:
                mid = (l + r) // 2
                if arr[mid][0] == timestamp:
                    return arr[mid][1]
                elif arr[mid][0] < timestamp:
                    l = mid + 1
                else:
                    r = mid
            return arr[l - 1][1]
        return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)