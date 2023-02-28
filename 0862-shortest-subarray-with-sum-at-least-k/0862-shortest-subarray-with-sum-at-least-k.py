class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefixSum = []
        prefixSum = list(accumulate(nums, initial=0))
        queue = deque()
        # queue.append(0)
        ans = float('inf')
        for idx , value in enumerate(prefixSum):
            
            while queue and value - prefixSum[queue[0]] >= k:
                ans = min(ans,idx - queue[0])
                queue.popleft()
            while queue and prefixSum[queue[-1]] >= value:
                queue.pop()
            
            queue.append(idx)
                
        if ans == float('inf'):
            return -1    
        return ans
 





    '''
test Cases
[1]
1
[1,2]
4
[2,-1,2]
3
[84,-37,32,40,95]
167
[77,19,35,10,-14]
19
[45,95,97,-34,-42]
21
[58,-27,-11,63,90,83,61,-44,-39,30]
61
[-40,-25,32,-19,61,45,50,83,79,74,-11,62,23,49,47,21,94,24,-19,90]
236
[56,-21,56,35,-9]
61
[11,47,97,35,-46,59,46,51,59,80,14,-6,2,20,96,1,18,74,-17,71]
282
[-36,10,-28,-42,17,83,87,79,51,-26,33,53,63,61,76,34,57,68,1,-30]
484
[-34,37,51,3,-12,-50,51,100,-47,99,34,14,-13,89,31,-14,-44,23,-38,6]
151
[39353,64606,-23508,5678,-17612,40217,15351,-12613,-37037,64183,68965,-19778,-41764,-21512,17700,-23100,77370,64076,53385,30915,18025,17577,10658,77805,56466,-2947,29423,50001,31803,9888,71251,-6466,77254,-30515,2903,76974,-49661,-10089,66626,-7065,-46652,84755,-37843,-5067,67963,92475,15340,15212,54320,-5286]
207007
'''
        
#         length = len(nums)
#         total = 0
#         ans = length + 1
#         left = 0
#         negativeCount = 0
#         print(nums, k)
    
#         for right in range(length):
#             if nums[right]< 0:
#                 if total <= abs(nums[right]):
#                     left = right + 1
#                     total = 0
#                     if right < length-1:
#                         right += 1
#                 else:   
#                     total += nums[right]
#                     negativeCount += 1
#             else:
#                 total += nums[right]
            
#             if left < right and nums[left] <= 0:
#                 total -= nums[left]
#                 left += 1
#                 negativeCount -= 1
#             print(left, right, total)
#             while left <= right and total >= k:
#                 if total >= k:
#                     ans = min( right-left + 1 , ans)
        
#                 while left <= right and nums[left] > 0  and (total>=k or negativeCount > 0):
#                     if total >= k:
#                         ans = min( right-left + 1 , ans)
                    
#                     total -= nums[left]
#                     left += 1
                
#                 while left <= right and (nums[left] <= 0 or total >= k) :
#                     if total >= k:
#                         ans = min( right-left + 1 , ans)
#                     if nums[left] < 0:
#                         negativeCount -= 1
#                     total -= nums[left]
#                     left += 1
#                 if left < right and total >= k:
#                     total -= nums[left]
#                     left += 1
        
#         if ans == length + 1:
#             return -1
        
#         return ans
        
    
        



