class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        ans = 0
        for num in gain:
            altitude += num
            ans = max(ans , altitude)
        return ans