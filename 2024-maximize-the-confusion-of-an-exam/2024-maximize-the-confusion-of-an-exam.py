class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans = 0
        left = 0
        count = 0
        for right , val in enumerate(answerKey):
            if val == "F":
                count += 1
            while count > k:
                if answerKey[left] == "F":
                    count -= 1
                left += 1
            
            ans = max(ans , right - left + 1)
        
        left = 0
        count = 0
        for right , val in enumerate(answerKey):
            if val == "T":
                count += 1
            while count > k:
                if answerKey[left] == "T":
                    count -= 1
                left += 1
            
            ans = max(ans , right - left + 1)
        
        return ans