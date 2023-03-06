class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        length = len(intervals)
        end_point = []
        for idx , (start , end) in enumerate(intervals):
            end_point.append([start,idx])
        end_point.sort()
        ans = []
        for start , end in intervals:
            left = -1
            right = length
            
            while left + 1 < right:
                mid = left + (right - left) // 2
                
                if end_point[mid][0] >= end:
                    right = mid
                else:
                    left = mid
            
            if right == length:
                ans.append(-1)
            else:
                ans.append(end_point[right][1])
        
        return ans