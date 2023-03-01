class Solution:
#     def winner(self, arr, left , right , p1Turn):       
#         if p1Turn :
#             if right == left:
#                 return [arr[right],0]
#             scoreLeft = self.winner(arr,left + 1 ,right , False)
#             scoreLeft[0] += arr[left]
#             scoreRight = self.winner(arr,left , right -1 , False)
#             scoreRight[0] += arr[right]
            
#             if scoreLeft[0] >= scoreRight[0]:
#                 return scoreLeft
#             else:
#                 return scoreRight
#         else :
#             if right == left:
#                 return [0,arr[right]]
#             scoreLeft = self.winner(arr,left + 1 ,right , True)
#             scoreLeft[1] += arr[left]
#             scoreRight = self.winner(arr,left , right -1 , True)
#             scoreRight[1] += arr[right]
            
#             if scoreLeft[1] >= scoreRight[1]:
#                 return scoreLeft
#             else:
#                 return scoreRight
        
       
    def winner(self, arr , left,right):
        if left == right :
            return arr[left]
        ans = max(arr[left] - self.winner(arr, left + 1 , right ),arr[right] - self.winner(arr,left,right - 1))
        
        return ans
        
        
    def PredictTheWinner(self, nums: List[int]) -> bool:
        right = len(nums) - 1
        score =  self.winner(nums , 0 , right)
        
        return score >= 0
    