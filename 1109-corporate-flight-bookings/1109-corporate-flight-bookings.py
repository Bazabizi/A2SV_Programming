class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefixSum = [0]*(n+1)
        for first , last , seat in bookings:
            prefixSum[first-1] += seat
            prefixSum[last ] -= seat
        
        prefixSum = list(accumulate(prefixSum))
        prefixSum.pop()
        return prefixSum
        