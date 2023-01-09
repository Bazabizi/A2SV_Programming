class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        countBox =[]
        size = len(boxes)
        
        for index in range(size):
            if boxes[index] =="1":
                countBox.append(index)
        
        ans=[]
        length = len(countBox)
        
        for idx in range(size):
            sum = 0
            for num in countBox:
                sum += abs(idx-num)
            ans.append(sum)
            
        return ans
                