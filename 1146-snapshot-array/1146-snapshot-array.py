class SnapshotArray:

    def __init__(self, length: int):       
        self.arr = [[[0 ,0]] for _ in range(length)]
        self.id = 0
        
    def set(self, index: int, val: int) -> None:
        self.arr[index].append([self.id , val])

    def snap(self) -> int:
        self.id += 1
        return self.id - 1
    
    def get(self, index: int, snap_id: int) -> int:
        arr = self.arr[index]
        left = -1
        right = len(arr)
        while left + 1 < right:
            mid = left + (right - left)//2
            
            if arr[mid][0] > snap_id:
                right = mid
            else:
                left = mid
        return arr[right -1][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)