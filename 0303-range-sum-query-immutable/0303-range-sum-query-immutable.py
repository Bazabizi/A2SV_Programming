class NumArray:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.prefixSum = list(accumulate(nums))
        self.prefixSum.insert(0,0)
        
    def sumRange(self, left: int, right: int) -> int:
        total = self.prefixSum[right+1] - self.prefixSum[left]
        return total
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)