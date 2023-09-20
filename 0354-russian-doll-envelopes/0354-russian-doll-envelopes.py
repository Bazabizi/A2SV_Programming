class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x: (x[0] , -x[1]))
        ans = 0
        arr = []
        for w , h in envelopes:
            if not arr or arr[-1] < h:
                ans += 1
                arr.append(h)
            else:
                left = -1
                right = len(arr)
                while left + 1 < right:
                    mid = left + (right - left)//2
                    
                    if arr[mid] >= h:
                        right = mid
                    else:
                        left = mid
                    
                arr[right] = h
        return ans