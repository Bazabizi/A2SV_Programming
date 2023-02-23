class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prefixSum = [0]*1002
        
        for operation , start ,destination in trips:
            prefixSum[start+1] += operation
            prefixSum[destination+1] -= operation
        
        for index in range(1,1002):
            prefixSum[index] += prefixSum[index-1]
            if prefixSum[index] > capacity:
                return False
        return True